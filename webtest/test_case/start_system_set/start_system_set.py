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


class SYSTEM_SET(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/SYSTEM_SET')

    def test_001_set_system_parameters(self):
        make_path.make_path('./screenshot/SYSTEM_SET/001')
        driver = self.driver
        success = 0
        try:
            print (u"系统参数设置")
            login.login(self)
            wait=WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="parameters"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[1]/tbody/tr[2]/td[2]/span/input[1]').send_keys(Keys.CONTROL,'a')  # 修改设备名称
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[1]/tbody/tr[2]/td[2]/span/input[1]').send_keys(Keys.BACK_SPACE)
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[1]/tbody/tr[2]/td[2]/span/input[1]').send_keys("test")
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys(Keys.CONTROL,'a')#修改终端超时
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys(Keys.BACK_SPACE)
            driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys("300")
            driver.find_element_by_id("submit").click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
            if driver.find_element_by_xpath('//*[@id="paramteEditForm"]/div/table[1]/tbody/tr[2]/td[2]/span/input[2]').get_attribute('value')=='test':
                success = 1
            else:
                success = 0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_SET\\001\error_set_system_parameters1.png")
            print('error:',e)
            success = 0

        finally:
            self.assertTrue(success,msg=u'system parameters set failed')
            logout.logout(self)

     # def test_002_set_system_time(self):
         # try:
             # u"系统时间设置"
             # driver=self.driver
             # time.sleep(1)
             # login.login(self)

             # driver.find_element_by_id("system_menu").click()
             # time.sleep(2)
             # driver.find_element_by_xpath("//*[@id='systemSet']/li[3]/a").click()
             # time.sleep(2)
             # driver.find_element_by_id('timeSet').click()
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys(Keys.CONTROL,'a')
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys(Keys.BACK_SPACE)
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys("2017-04-01")
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[2]/input[1]').send_keys(Keys.CONTROL,'a')
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[2]/input[1]').send_keys(Keys.BACK_SPACE)
             # time.sleep(1)
             # driver.find_element_by_xpath('//*[@id="panelBox"]/div/table[2]/tbody/tr[2]/td[2]/span[2]/input[1]').send_keys("00:00:00")
             # time.sleep(1)
             # driver.find_element_by_id("submit").click()
             # time.sleep(2)
             # success = 1

         # except Exception as e:
             # driver.get_screenshot_as_file(".\screenshot\error_set_system_time1.png")
             # print('error:',e)
             # success = 0

         # finally:
             # self.assertTrue(success,msg='system time set failed')
             # logout.logout(self)

    def test_003_set_system_service(self):
        make_path.make_path('./screenshot/SYSTEM_SET/003')
        driver = self.driver
        success = 0
        try:
            print (u"本地服务设置")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="serviceSet"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'sshd')))
            text_1=driver.find_element_by_id('sshd').get_attribute('title')
            driver.find_element_by_id('sshd').click()
            time.sleep(2)
            text_2=driver.find_element_by_id('sshd').get_attribute('title')
            text_3 = driver.find_element_by_id('telnetd').get_attribute('title')
            driver.find_element_by_id('telnetd').click()
            time.sleep(2)
            text_4 = driver.find_element_by_id('telnetd').get_attribute('title')
            if text_1 != text_2 and text_3 != text_4:
                success = 1
            else:
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_SET\\003\error_set_system_service.png")
            time.sleep(2)

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_SET\\003\error_set_system_service1.png")
            print('error:',e)
            success = 0

        finally:
            self.assertTrue(success,msg = 'set local service failed')
            logout.logout(self)



    def test_004_diagnose(self):
        make_path.make_path('./screenshot/SYSTEM_SET/004')
        driver = self.driver
        success = 0
        try:
            print (u"系统诊断")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="diagnose"]/div[1]'))).click()
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='diagnoForm']/table/tbody/tr[2]/td[2]/span/input[1]").send_keys("192.168.98.156")
            time.sleep(1)
            driver.find_element_by_id("diagnoseStart1").click()
            time.sleep(5)
            success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_SET\\004\error_system_diagnose1.png")
            print('error:',e)
            success = 0

        finally:
            self.assertTrue(success,msg = 'system diagnose failed')
            logout.logout(self)

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
