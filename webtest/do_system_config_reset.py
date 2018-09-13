# coding=UTF-8
import telnetlib
import time
import sys
import json
import re
sys.path.append("\ public")


# 此文件用于重置系统配置
def config_reset():
    # 获取串口信息
    file_1 = '.\config\console.json'  # 相对路径是以执行文件的目录为基准
    with open(file_1, 'r') as a:
        b = json.load(a)
        host = b['host']
        port = b['port']
        user = str(b['username'])
        password = str(b['password'])
    # 获取设备管理口信息
    file_2 = '.\config\device.json'  # 相对路径是以执行文件的目录为基准
    with open(file_2, 'r') as c:
        d = json.load(c)
        dev_ip = str(d['dev_ip'])
        dev_mask = str(d['dev_mask'])
        gateway = str(d['gateway'])

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
    tn.read_until('#', timeout=10)
    tn.write('system config reset \n')
    tn.read_until('#', timeout=10)
    tn.write('network reset \n')
    tn.read_until('#', timeout=10)
    tn.write('network interface feth0 ip add ' + dev_ip + ' mask ' + dev_mask + '\n')
    tn.read_until('#', timeout=10)
    tn.write('network route add dst 172.18.0.0/16 gw ' + gateway + '\n')
    tn.read_until('#', timeout=10)
    tn.write('network route add dst 192.168.0.0/16 gw ' + gateway + '\n')
    tn.read_until('#', timeout=10)
    tn.write('save all-vsys\n')
    tn.read_until('#', timeout=10)
    tn.write('\n')
    tn.read_until('#', timeout=10)
    tn.write('exit\n')
    time.sleep(1)
    tn.read_until('Save system config?[y/n]:', timeout=5)
    time.sleep(1)
    tn.write('n\n')
    tn.write('\n')

if __name__=='__main__':
    config_reset()
