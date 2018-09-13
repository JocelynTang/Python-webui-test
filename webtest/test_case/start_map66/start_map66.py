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


class MAP66(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/MAP66')

    def test_001_add_addresses(self):
        make_path.make_path('./screenshot/MAP66/001')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加地址对象""")
            login.login(self)
            match_1 = 0
            match_2 = 0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID,'policy_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="object"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]'))).click()
            driver.find_element_by_xpath('//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("source_v6")
            driver.find_element_by_id('typeSubnet').click()
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[1]/input[1]').send_keys("1000::")
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[2]/input[1]').send_keys('64')
            driver.find_element_by_id("submitAddress").click()
            time.sleep(3)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]'))).click()
            driver.find_element_by_xpath('//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("destination_v6")
            driver.find_element_by_id('typeSubnet').click()
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[1]/input[1]').send_keys("2000::")
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[2]/input[1]').send_keys('64')
            driver.find_element_by_id("submitAddress").click()
            time.sleep(3)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') =='name':
                    text=input_1.text
                    if text=="source_v6":
                        match_1 = 1
                        break

            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') =='name':
                    text=input_2.text
                    if text=="destination_v6":
                        match_2 = 1
                        break

            if match_1==1 and match_2==1:
                print ("Add addresses successfully!")
                success = 1
            else:
                print ("Add addresses failed!")
                driver.get_screenshot_as_file(".\screenshot\MAP66\\001\error_add_addresses_map66.png")
                success =0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\MAP66\\001\error_add_addresses_map66_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add addresses failed')

    def test_002_add_map66(self):
        make_path.make_path('./screenshot/MAP66/002')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u'添加MAP66')
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MAP66"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MAP66"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addMap66Btn'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="map66Form"]/div[1]/table/tbody/tr[3]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="map66Form"]/div[1]/table/tbody/tr[3]/td[2]/span/input[1]').send_keys('source_v6')
            driver.find_element_by_xpath('//*[@id="orgTr"]/td[2]/span/input[1]').send_keys('destination_v6')
            time.sleep(1)
            driver.find_element_by_id('map66Submit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addMap66Btn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='orig_src':
                    text=input.text
                    if text=="source_v6":
                        match = 1
                        break
            if (not match):
                print ("Add map66 failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\MAP66\\002\error_add_map66.png")
            else:
                print ("Add map66 successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\MAP66\\002\error_add_map66_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add map66 failed')

    def test_003_delete_map66(self):
        make_path.make_path('./screenshot/MAP66/003')
        success = 0
        driver = self.driver
        time.sleep(1)
        try:
            print (u"删除MAP66")
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MAP66"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MAP66"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearMap66Btn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addMap66Btn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'orig_src':
                    text = input.text
                    if text == "source_v6":
                        match = 1
                        break
            if (match):
                print ("Clear map66 failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\MAP66\\003\error_clear_map66.png")
            else:
                print ("Clear map66 successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\MAP66\\003\error_delete_map66_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete map66 failed')

    def test_004_clear_addresses(self):
        make_path.make_path('./screenshot/MAP66/004')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""清空地址对象""")
            login.login(self)

            match_1 = 0
            match_2 = 0

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') =='name':
                    text=input_1.text
                    if text=="source_v6":
                        match_1 = 1
                        break

            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') =='name':
                    text=input_2.text
                    if text=="destination_v6":
                        match_2 = 1
                        break

            if match_1==0 and match_2==0:
                print ("Clear addresses successfully!")
                success = 1
            else:
                print ("Clear addresses failed!")
                driver.get_screenshot_as_file(".\screenshot\MAP66\\004\error_clear_addresses_map66.png")
                success =0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\MAP66\\004\error_clear_addresses_map66_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'clear address failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

