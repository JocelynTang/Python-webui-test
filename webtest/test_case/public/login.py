# coding=UTF-8
import time
import json
from selenium import webdriver


# 此文件用来登录webui，登录信息都存在logininfo.json文件中，根据不同浏览器的不同情况，选择不同的处理方式
def login(self):
    file = '.\config\logininfo.json'# 相对路径是以执行文件的目录为基准
    with open(file,'r') as a:
        b = json.load(a)
        url = b['url']
        user = b['username']
        password = b['password']
        browser = b['browser']
    try:
        driver = self.driver
        self.url = url
        self.user = user
        self.password = password
        self.browser = browser

        if self.browser == 'ie':
            try:
                driver.get(self.url)
                driver.get("javascript:document.getElementById('overridelink').click();")
                time.sleep(1)
                driver.maximize_window()
                print ('browser: ie')
                time.sleep(2)
                # driver.find_element_by_id('name').clear()
                driver.find_element_by_id('name').send_keys(self.user)
                # driver.find_element_by_id('password').clear()
                driver.find_element_by_id('password').send_keys(self.password)
                driver.find_element_by_id("code").send_keys("12df")
                time.sleep(1)
                driver.find_element_by_id('submit').click()
                # driver.get("javascript:document.getElementById('submit').click();")
                time.sleep(20)

            except Exception as e:
                print('error:', e)

        elif self.browser == 'chrome':
            try:
                # options=webdriver.ChromeOptions()
                # options.add_argument('--ignore-certificate-erros')
                # driver=webdriver.Chrome(chrome_options=options)
                driver.get(self.url)
                # driver.get("javascript:document.getElementById('overridelink').click();")
                time.sleep(1)
                driver.maximize_window()
                print ('browser: chrome')
                time.sleep(2)
                # driver.find_element_by_id('name').clear()
                driver.find_element_by_id('name').send_keys(self.user)
                # driver.find_element_by_id('password').clear()
                driver.find_element_by_id('password').send_keys(self.password)
                driver.find_element_by_id("code").send_keys("12df")
                time.sleep(1)
                driver.find_element_by_id('submit').click()
                # driver.get("javascript:document.getElementById('submit').click();")
                time.sleep(10)
            except Exception as e:
                print('error:', e)

        elif self.browser == 'firefox':
            try:
                driver.get(self.url)
                time.sleep(1)
                driver.maximize_window()
                print ('browser: firefox')
                time.sleep(2)
                # driver.find_element_by_id('name').clear()
                driver.find_element_by_id('name').send_keys(self.user)
                # driver.find_element_by_id('password').clear()
                driver.find_element_by_id('password').send_keys(self.password)
                driver.find_element_by_id("code").send_keys("12df")
                time.sleep(1)
                driver.find_element_by_id('submit').click()
                time.sleep(20)

            except Exception as e:
                print('error:', e)

    except Exception as e:
        print(e)
    finally:
        pass

