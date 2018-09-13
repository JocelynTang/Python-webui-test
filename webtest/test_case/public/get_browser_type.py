# coding=utf-8
import json
from selenium import webdriver


# 此文件用于读取配置文件设置测试时使用的浏览器类型
def set_browser():
    config_file = '.\config\logininfo.json'  # 相对路径是以执行文件的目录为基准
    with open(config_file, 'r') as a:
        b = json.load(a)
        browser = b['browser']
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        # 处理Firefox下载文件时需要选择存储路径的问题
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', 'C:\Users\\admin\Downloads')
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'application/x-gtar,application/a-gzip,application/x-gzip,application/x-gzip,'
                               'application/zip,application/x-gtar,text/plain,application/x-compressed,'
                               'application/octet-stream,application/pdf')
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        print('unrecognized browser type, please check your configuration file!!!')
        driver = []

    return driver
