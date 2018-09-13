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


class NAT(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/NAT')

    def test_001_add_addr(self):
        make_path.make_path('./screenshot/NAT/001')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加地址对象""")
            login.login(self)
            match_1 = 0
            match_2 = 0
            match_3 = 0

            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 地址
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(2)
            # 添加地址对象
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]'))).send_keys("source")
            driver.find_element_by_id('typeSubnet').click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="addr3"]/td/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[1]/input[1]').send_keys("3.3.3.0")
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[2]/input[1]').send_keys('24')
            driver.find_element_by_id("submitAddress").click()
            time.sleep(3)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("destination")
            driver.find_element_by_id('typeSubnet').click()
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[1]/input[1]').send_keys("4.4.4.0")
            driver.find_element_by_xpath('//*[@id="addr3"]/td/span[2]/input[1]').send_keys('24')
            driver.find_element_by_id("submitAddress").click()
            time.sleep(3)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("host")
            driver.find_element_by_id('typeHost').click()
            driver.find_element_by_xpath('//*[@id="hostAddr"]/tbody/tr/td/span/input[1]').send_keys("4.4.4.2")
            driver.find_element_by_id("submitAddress").click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') =='name':
                    text=input_1.text
                    if text=="source":
                        match_1 = 1
                        break

            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') =='name':
                    text=input_2.text
                    if text=="destination":
                        match_2 = 1
                        break

            inputs_3 = driver.find_elements_by_tag_name('td')
            for input_3 in inputs_3:
                if input_3.get_attribute('field') =='name':
                    text=input_3.text
                    if text=="host":
                        match_3 = 1
                        break

            if match_1==1 and match_2==1 and match_3==1:
                print ("Add addresses successfully!")
                success = 1
            else:
                print ("Add addresses failed!")
                driver.get_screenshot_as_file(".\screenshot\NAT\\001\error_add_addresses_nat.png")
                success =0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\NAT\\001\error_add_addresses_nat_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg='add addresses failed')

    def test_002_add_nat(self):
        make_path.make_path('./screenshot/NAT/002')
        driver = self.driver
        success = 0
        try:
            print (u"""添加NAT策略""")
            login.login(self)
            wait = WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID,'policy_menu'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(7)
            wait.until(EC.element_to_be_clickable((By.ID, 'mode2'))).click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="natForm"]/div[1]/table/tbody/tr[5]/td[2]/span/input[1]').send_keys('source')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="natForm"]/div[1]/table/tbody/tr[11]/td[2]/span/input[1]').send_keys('destination')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="transTr"]/td[2]/span/span/a').click()
            time.sleep(1)
            hs = driver.find_elements_by_tag_name('span')
            for h in hs:
                if h.get_attribute('class')=='tree-title':
                    text=h.text
                    if text=='host':
                        h.click()
                        break
            time.sleep(2)
            driver.find_element_by_id('addNat').click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='orig_src':
                    text=input.text
                    if text=="source":
                        match = 1
                        break
            if (not match):
                print ("Add nat failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\NAT\\002\error_add_nat.png")
            else:
                print ("Add nat successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\NAT\\002\error_add_nat1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg='add nat failed')

    def test_003_clear_nat(self):
        make_path.make_path('./screenshot/NAT/003')
        driver = self.driver
        success = 0
        try:
            print (u"""清空NAT策略""")
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID,'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'orig_src':
                    text = input.text
                    if text == "source":
                        match = 1
                        break
            if (match):
                print ("clear nat failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\NAT\\003\error_clear_nat.png")
            else:
                print ("clear nat successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\NAT\\003\error_clear_nat_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg='clear nat failed')

    def test_004_clear_addr(self):
        make_path.make_path('./screenshot/NAT/004')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""清空地址对象""")

            login.login(self)
            match_1 = 0
            match_2 = 0
            match_3 = 0

            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 地址
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(1)
            # 添加地址对象
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') =='name':
                    text=input_1.text
                    if text=="source":
                        match_1 = 1
                        break

            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') =='name':
                    text=input_2.text
                    if text=="destination":
                        match_2 = 1
                        break

            inputs_3 = driver.find_elements_by_tag_name('td')
            for input_3 in inputs_3:
                if input_3.get_attribute('field') =='name':
                    text=input_3.text
                    if text=="host":
                        match_3 = 1
                        break

            if match_1==0 and match_2==0 and match_3==0:
                print ("Clear addresses successfully!")
                success = 1
            else:
                print ("Clear addresses failed!")
                driver.get_screenshot_as_file(".\screenshot\NAT\\004\error_clear_addresses_nat.png")
                success =0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\NAT\\004\error_clear_addr_nat_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'clear address failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

