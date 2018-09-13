#coding=utf-8
import telnetlib
import time


def do_telnet(Host,user,password,finish,commands):
    tn=telnetlib.Telnet(Host,port=23,timeout=10)
    tn.set_debuglevel(2)
    tn.read_until('login: ')
    tn.write(user+'\n')
    tn.read_until('Password: ')
    tn.write(password+'\n')
    tn.read_until(finish)
    for command in commands:
        tn.write('%s\n'%command)
    time.sleep(10)
    tn.read_until(finish)
    tn.write('exit\n')

# if __name__=='__main__':
#     Host='172.18.20.182'
#     user='root'
#     password='root1130@ngfw'
#     finish='-sh-3.2# '
#     commands=['cd /SE',
#               'pwd',
#               'cp login.html /usr/local/apache2/htdocs/Application/Home/View/Index',
#               'cp IndexController.class.php /usr/local/apache2/htdocs/Application/Home/Controller',
#               'cd /usr/local/apache2/htdocs/Application/Home/View/Index',
#               'ls',
#               'cd /usr/local/apache2/htdocs/Application/Home/Controller',
#               'ls',
#               ]
#     do_telnet(Host,user,password,finish,commands)