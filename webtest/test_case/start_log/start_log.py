# coding=UTF-8
from selenium import webdriver
import unittest
import time
from test_case.public import *
import sys
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append("\ public")

success = 0


class LOG(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/LOG')

    def test_001_clear_log(self):
        make_path.make_path('./screenshot/LOG/001')
        driver = self.driver
        success = 0
        try:
            print (u"""清空管理员登陆日志""")
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logShow"]/div[1]'))).click()
            time.sleep(1)
            # 审计日志
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="audti"]/div[1]'))).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="panelBox"]/div[1]/div[1]/span/span'))).click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == u"管理员登录日志":
                        type.click()
                        break
            driver.find_element_by_xpath('//*[@id="panelBox"]/div[1]/div[2]').click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(4)
            wait.until(EC.element_to_be_clickable((By.ID,'clearBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "id":
                    text = input.text
                    if text == "NGTOS":
                        match = 1
                        break
            if (match):
                success = 0
                driver.get_screenshot_as_file(".\screenshot\LOG\\001\error_clear_log.png")
                print ('failed to clear log')
            else:
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\LOG\\001\error_clear_log1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='clear log failed')

    def test_002_log_set(self):
        make_path.make_path('./screenshot/LOG/002')
        driver = self.driver
        success = 0
        try:
            print (u"""日志配置""")

            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logsSet"]/div[1]'))).click()
            # 日志配置
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logSet"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'allConfigChecked'))).click()
            driver.find_element_by_id('lowId').click()#级别严重程度：低
            target=driver.find_element_by_id('logSetSubmit')
            driver.execute_script('arguments[0].scrollIntoView();',target)
            driver.find_element_by_id("logSetSubmit").click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID,'allConfigChecked')))
            ck = driver.find_element_by_id('allConfigChecked').get_attribute('checked')
            if (ck):
                success = 1
            else:
                success = 0
                print('log set failed')
                driver.get_screenshot_as_file(".\screenshot\LOG\\002\error_log_set.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\LOG\\002\error_log_set1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='log set failed')

    def test_003_logserver_set(self):
        make_path.make_path('./screenshot/LOG/003')
        success = 0
        driver = self.driver
        try:
            print (u"""日志服务器配置""")
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logsSet"]/div[1]'))).click()
            time.sleep(1)
            # 日志服务器配置
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logServer"]/div[1]'))).click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="serverAddr"]/div/span/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="serverAddr"]/div/span/input[1]').send_keys("192.168.98.156")
            driver.find_element_by_xpath('//*[@id="logSetForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(Keys.CONTROL,'a')
            driver.find_element_by_xpath('//*[@id="logSetForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(Keys.BACK_SPACE)
            driver.find_element_by_xpath('//*[@id="logSetForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys("1234")
            # driver.find_element_by_id("toConsole").click()
            # time.sleep(1)
            driver.find_element_by_id("toDatabase").click()
            driver.find_element_by_id("trans").click()
            driver.find_element_by_id("logServerSubmit").click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID,'logServerSubmit')))
            text=driver.find_element_by_id('trans').get_attribute('checked')
            if text:
                print ('set log server successfully')
                success = 1
            else:
                print ('set log server failed')
                success = 0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\LOG\\003\error_log_server_set1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='set log server failed')

    def test_004_view_the_log(self):
        make_path.make_path('./screenshot/LOG/004')
        driver = self.driver
        success = 0
        try:
            print (u"""查看管理员登录日志""")
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logShow"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="audti"]/div[1]'))).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="panelBox"]/div[1]/div[1]/span/span'))).click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == u"管理员登录日志":
                        type.click()
                        break
            driver.find_element_by_xpath('//*[@id="panelBox"]/div[1]/div[2]').click()
            time.sleep(2)

            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "id":
                    text = input.text
                    if text == "NGTOS":
                        match = 1
                        break

            if (not match):
                print ("Load log failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\LOG\\004\error_view_the_log.png")
            else:
                print ("Load log successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\LOG\\004\error_view_the_log1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='view the log failed')

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()
