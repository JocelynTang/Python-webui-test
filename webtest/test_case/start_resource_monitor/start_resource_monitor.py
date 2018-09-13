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


class MONITOR(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/MONITOR')

    def test_001_monitor_config_set(self):
        make_path.make_path('./screenshot/MONITOR/001')
        driver = self.driver
        success = 0
        try:
            print (u"资源监控设置")
            login.login(self)
            wait=WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID,'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sysMaintain"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="resourceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys('1')
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="resourceForm"]/table/tbody/tr[4]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[4]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[4]/td[2]/span[1]/input[1]').send_keys('1')
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="resourceForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').send_keys('1')
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="resourceForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="resourceForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]').send_keys('900000')
            driver.find_element_by_id('disable').click()
            driver.find_element_by_id('submit').click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource"]/div[1]'))).click()
            time.sleep(1)
            text=driver.find_element_by_id('disable').get_attribute('checked')
            if text:
                print ('system monitor config set successfully!!!')
                success = 1
            else:
                print ('system monitor config set failed!!!')
                driver.get_screenshot_as_file(".\screenshot\MONITOR\\001\error_monitor_config_set.png")
                success = 0

        except Exception as e:
            print('error:',e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\MONITOR\\001\error_monitor_config_set_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='monitor config set failed')

    def test_002_close_monitor(self):
        make_path.make_path('./screenshot/MONITOR/002')
        driver = self.driver
        success = 0
        try:
            print (u"关闭资源监控")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sysMaintain"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource"]/div[1]'))).click()
            time.sleep(1)
            driver.find_element_by_id('enable').click()
            time.sleep(1)
            driver.find_element_by_id('submit').click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource"]/div[1]'))).click()
            time.sleep(1)
            text=driver.find_element_by_id('enable').get_attribute('checked')
            if text:
                print ('close monitor successfully!!!')
                success = 1
            else:
                print ('close monitor failed!!!')
                driver.get_screenshot_as_file(".\screenshot\MONITOR\\002\error_close_monitor.png")
                success = 0

        except Exception as e:
            print('error:',e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\MONITOR\\002\error_close_monitor_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='close monitor failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
