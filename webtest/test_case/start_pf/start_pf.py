# coding=UTF-8
from selenium import webdriver
import unittest
import time
from test_case.public import *
import sys
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append("\ public")


class PF(unittest.TestCase):
    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/PF')

    def test_001_add_pf_service(self):
        print (u"添加pf")
        make_path.make_path('./screenshot/PF/001')
        driver = self.driver
        success = 0
        try:
            login.login(self)
            match = 0
            wait=WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID,'system_menu'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pf"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="nameSelect"]/span/input[1]').send_keys('tp')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="pfForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('area_feth0')
            time.sleep(2)
            driver.find_element_by_id('addSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='name':
                    text_1=input.text
                    if text_1=='tp':
                        match = 1
                        break
            if match:
                print ('add pf service successfully!!!')
                success = 1
            else:
                print ('add pf service failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\PF\\001\error_add_pf_service.png")

        except Exception as e:
            print('error:',e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\PF\\001\error_add_pf_service_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Add pf service failed')

    def test_002_edit_pf_service(self):
        print (u"编辑pf")
        make_path.make_path('./screenshot/PF/002')
        driver = self.driver
        success = 0
        try:
            login.login(self)
            match_1 = 0
            match_2 = 0
            time.sleep(2)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="pf"]/div[1]').click()
            time.sleep(2)

            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'name':
                    text_1 = input_1.text
                    if text_1 == 'tp':
                        input_1.click()
                        match_1 = 1
                        break
            if match_1:
                driver.find_element_by_id('editBtn').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="nameSelect"]/span/input[1]').clear()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="nameSelect"]/span/input[1]').send_keys('dhcp')
                time.sleep(2)
                driver.find_element_by_id('addSubmit').click()
                time.sleep(2)
            else:
                print ('failed to find pf service!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\PF\\002\error_edit_pf_service.png")
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field')=='name':
                    text_2 = input_2.text
                    if text_2 == 'dhcp':
                        match_2 = 1
                        break
            if match_2:
                print ('edit pf service successfully!!!')
                success = 1
            else:
                print ('edit pf service failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\PF\\002\error_edit_pf_service_1.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\PF\\002\error_edit_pf_service_2.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Edit pf service failed')

    def test_003_delete_pf_service(self):
        print (u"删除pf")
        make_path.make_path('./screenshot/PF/003')
        driver = self.driver
        success = 0
        try:
            login.login(self)
            match_1 = 0
            match_2 = 0
            time.sleep(2)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="pf"]/div[1]').click()
            time.sleep(2)

            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'name':
                    text_1 = input_1.text
                    if text_1 == 'dhcp':
                        input_1.click()
                        match_1 = 1
                        break
            if match_1:
                driver.find_element_by_id('deleteBtn').click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(5)
            else:
                print ('failed to find pf service!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\PF\\003\error_delete_pf_service.png")
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') == 'name':
                    text_2 = input_2.text
                    if text_2 == 'dhcp':
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ('delete pf service successfully!!!')
                success = 1

            else:
                print ('delete pf service failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\PF\\003\error_delete_pf_service.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\PF\\003\error_delete_pf_service_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Delete pf service failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
