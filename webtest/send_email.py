# coding=utf-8
from sgmllib import SGMLParser
import os
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import zipfile
import telnetlib
import json
import re
import urllib2
import time


# 将截图压缩
def add_zipfile():
    z = zipfile.ZipFile('screenshot.zip', 'w', zipfile.ZIP_DEFLATED)
    startdir = "./screenshot"
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            z.write(os.path.join(dirpath, filename))
    z.close()
    return 'screenshot.zip'


# 获取最新的HTML文件
def get_htmlfile():
    result_dir = '.\\report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    print (u'最新的文件为： ' + lists[-1])
    htmlfile = os.path.join(result_dir, lists[-1])
    return htmlfile


# 获取设备版本
def get_tos_version():
    file = '.\config\console.json'  # 相对路径是以执行文件的目录为基准
    with open(file, 'r') as a:
        b = json.load(a)
        host = b['host']
        port = b['port']
        user = str(b['username'])
        password = str(b['password'])
    try:
        tn = telnetlib.Telnet(host, port, timeout=10)
        tn.set_debuglevel(2)
        tn.write('\n')
        res = tn.read_until('#', timeout=5)
        if re.search('root@localhost', res):
            tn.write('login ' + user + '\n')
            tn.read_until('Password: ', timeout=5)
            tn.write(password + '\n')
            tn.read_until('#', timeout=5)
        elif re.search('Topsec Operating System', res):
            tn.read_until('login: ', timeout=5)
            tn.write(user + '\n')
            tn.read_until('Password: ', timeout=5)
            tn.write(password + '\n')
            tn.read_until('#', timeout=5)
        else:
            pass
        tn.write('\n')
        tn.read_until('#')
        tn.write('system version\n')
        t = tn.read_until('haveroot', timeout=5)
        tn.write('\n')
        tn.read_until('# ', timeout=5)
        tn.write('exit\n')
        time.sleep(1)
        tn.read_until('Save system config?[y/n]:', timeout=5)
        time.sleep(1)
        tn.write('n\n')
        tn.write('\n')
        message = t.split(':')
        version = message[1]
        return version
    except Exception as e:
        print (e)


# 获取测试报告中的数据，包括测试开始时间、用时、用例执行情况
class GetIdList(SGMLParser):
    def reset(self):
        self.IDlist = []
        self.flag = False
        self.getdata = False
        self.verbatim = 0
        SGMLParser.reset(self)

    def start_div(self, attrs):
        if self.flag == True:
            self.verbatim +=1 #进入子层div了，层数加1
            return
        for k,v in attrs:#遍历div的所有属性以及其值
            if k == 'class' and v == 'heading':#确定进入了<div class='entry-content'>
                self.flag = True
                return

    def end_div(self):#遇到</div>
        if self.verbatim == 0:
            self.flag = False
        if self.flag == True:#退出子层div了，层数减1
            self.verbatim -=1

    def start_p(self, attrs):
        if self.flag == False:
            return
        for k,v in attrs:
            if k == 'class' and v == 'attribute':
                self.getdata = True
                return

    def end_p(self):#遇到</p>
        if self.getdata:
            self.getdata = False

    def handle_data(self, text):#处理文本
        if self.getdata:
            self.IDlist.append(text)
        return self.IDlist

    def printID(self):
        for i in self.IDlist:
            print (i)


# 发送邮件
def send_mail(zipfile, htmlfile, text, version):
    file_names = [zipfile, htmlfile]
    # 从配置文件中获取收发邮件需要用到的账号信息
    file = '.\config\email.json'
    with open(file, 'r') as a:
        b = json.load(a)
        sender = b['username']
        receiver = b['receiver']
        username = b['username']
        password = b['password']
        email_server = b['email_server']
        port = b['port']

    subject = str(version) + u' webui 测试报告'
    server = smtplib.SMTP(email_server, port)
    server.login(username, password)  # 仅smtp服务器需要验证时

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = MIMEText(text)
    main_msg.attach(text_msg)

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    # 读入文件内容并格式化
    for file_name in file_names:
        data = open(file_name, 'rb')
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.Encoders.encode_base64(file_msg)
        # 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename=basename)
        main_msg.attach(file_msg)

    # 设置根容器属性
    main_msg['From'] = sender
    main_msg['To'] = ','.join(receiver)
    main_msg['Subject'] = subject
    main_msg['Date'] = email.Utils.formatdate()

    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    server.sendmail(sender, receiver, fullText)
    server.quit()

    print ('email has sent out !')

def send_email():
    # 读取配置文件内容，决定是否需要发送邮件
    file = '.\config\email.json'
    with open(file, 'r') as a:
        b = json.load(a)
        switch = b['switch']
    if switch == 'off':
        pass
    elif switch == 'on':
        # 获取截图文件
        file1 = add_zipfile()
        # 获取测试报告
        file2 = get_htmlfile()
        # 获取当前测试版本
        version = get_tos_version()
        # 添加邮件内容：用例执行情况
        object_file = "file:\\" + os.path.abspath(file2)
        content = urllib2.urlopen(object_file).read()
        lister = GetIdList()
        text = lister.feed(content)
        results = lister.handle_data(text)
        information = ','.join(results)
        # 发送邮件
        send_mail(file1, file2, information, version)
    else:
        print('unrecognized paramater')

# if __name__ == "__main__":
    # try:
    #     send_email()
    # except Exception as E:
    #     print E

