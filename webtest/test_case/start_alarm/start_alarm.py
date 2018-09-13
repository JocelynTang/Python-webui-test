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


class ALARM(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/ALARM')

    def test_001_add_email(self):
        make_path.make_path('./screenshot/ALARM/001')
        driver = self.driver
        success = 0
        try:
            print (u"添加邮件告警")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="alarmNameTr"]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="alarmNameTr"]/td[2]/span/input[1]').send_keys('email1')
            driver.find_element_by_xpath('//*[@id="email1"]/td[2]/span/input[1]').send_keys('192.168.66.9')
            driver.find_element_by_xpath('//*[@id="email2"]/td[2]/span[1]/input[1]').send_keys('25')
            driver.find_element_by_xpath('//*[@id="email3"]/td[2]/p/span/input[1]').send_keys('tang_qiaoling@topsec.com.cn')
            driver.find_element_by_id('addEmail').click()
            driver.find_element_by_xpath('//*[@id="email4"]/td[2]/span/input[1]').send_keys('tos_alarm')
            driver.find_element_by_id('addAlarmSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='noticename':
                    text = input.text
                    if text=='email1':
                        match = 1
                        break
            if match:
                print ('add email successfully')
                success = 1
            else:
                print ('add email failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\ALARM\\001\error_add_email.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\001\error_add_email_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add email failed')

    def test_002_add_beep(self):
        make_path.make_path('./screenshot/ALARM/002')
        driver = self.driver
        success = 0
        try:
            print (u"添加声音告警")
            match=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'alarm_type2'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarmNameTr"]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="alarmNameTr"]/td[2]/span/input[1]').send_keys('beep1')
            driver.find_element_by_id('beepDefault').click()
            driver.find_element_by_id('addAlarmSubmit').click()
            time.sleep(3)
            #检查是否添加成功
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='noticename':
                    text = input.text
                    if text=='beep1':
                        match = 1
                        break
            if match:
                print ('add beep successfully')
                success = 1
            else:
                print ('add beep failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\ALARM\\002\error_add_beep.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\002\error_add_beep_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add beep failed')

    def test_003_add_console(self):
        make_path.make_path('./screenshot/ALARM/003')
        driver = self.driver
        success = 0
        try:
            print (u"添加控制台告警")
            match=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'alarm_type4'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarmNameTr"]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="alarmNameTr"]/td[2]/span/input[1]').send_keys('console1')
            driver.find_element_by_id('addAlarmSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='noticename':
                    text = input.text
                    if text=='console1':
                        match = 1
                        break
            if match:
                print ('add console successfully')
                success = 1
            else:
                print ('add console failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\ALARM\\003\error_add_console.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\003\error_add_console_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add console failed')

    def test_004_add_SNMP(self):
        make_path.make_path('./screenshot/ALARM/004')
        driver = self.driver
        success = 0
        try:
            print (u"添加SNMP告警")
            match=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'alarm_type5'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarmNameTr"]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="alarmNameTr"]/td[2]/span/input[1]').send_keys('SNMP1')
            driver.find_element_by_id('addAlarmSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='noticename':
                    text = input.text
                    if text=='SNMP1':
                        match = 1
                        break
            if match:
                print ('add SNMP successfully')
                success = 1
            else:
                print ('add SNMP failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\ALARM\\004\error_add_SNMP.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\004\error_add_SNMP_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add SNMP failed')

    def test_005_add_sms(self):
        make_path.make_path('./screenshot/ALARM/005')
        driver = self.driver
        success = 0
        try:
            print (u"添加短信告警")
            match=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'alarm_type6'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarmNameTr"]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="alarmNameTr"]/td[2]/span/input[1]').send_keys('sms1')
            driver.find_element_by_xpath('//*[@id="bios3"]/td[2]/span/input[1]').send_keys('18862061152')
            driver.find_element_by_xpath('//*[@id="bios4"]/td[2]/span[1]/input[1]').send_keys('60')
            time.sleep(1)
            driver.find_element_by_id('addAlarmSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='noticename':
                    text = input.text
                    if text=='sms1':
                        match = 1
                        break
            if match:
                print ('add sms successfully')
                success = 1
            else:
                print ('add sms failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\ALARM\\005\error_add_sms.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\005\error_add_sms_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add sms failed')

    def test_006_clear_all(self):
        make_path.make_path('./screenshot/ALARM/006')
        driver = self.driver
        success = 0
        try:
            print (u"清空告警")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alarm"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alarm"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn')))
            success = 1

            # inputs=driver.find_elements_by_tag_name('td')
            # for input in inputs:
            #     if input.get_attribute('field')=='noticename':
            #         text = input.text
            #         if text=='sms_1':
            #             match = 1
            #             break
            # if match:
            #     print 'add sms successfully'
            #     success = 1
            # else:
            #     print 'add sms failed'
            #     success = 0
            #     driver.get_screenshot_as_file('.\screenshot\error_add_sms.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ALARM\\006\error_clear_all_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='clear all failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()