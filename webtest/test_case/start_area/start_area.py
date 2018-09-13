#coding=UTF-8
from selenium import webdriver
import unittest
import time
import json
from test_case.public import *
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append("\ public")


class AREA(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/AREA')

    def test_001_add_area(self):
        make_path.make_path('./screenshot/AREA/001')
        driver = self.driver
        success=0
        try:
            print (u"""添加区域对象""")
            login.login(self)

            match = 0
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 区域
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="area"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="area"]/div[1]'))).click()
            time.sleep(1)
            # 添加区域对象
            wait.until(EC.element_to_be_clickable((By.ID,'addRegionBtn'))).click()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,'//*[@id="regionForm"]/div[1]/table/tbody/tr[1]/td[2]/span/input[1]'))).send_keys('area_test')
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="leftSelectItemCid"]/option[2]'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupLeft'))).click()
            driver.find_element_by_id('addRegion').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID,'addRegionBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="area_test":
                        match=1
                        break
            if (not match):
                print ("add area failed")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\AREA\\001\error_area_add.png")
            else:
                print ("Add area successfully!!!")
                success = 1

        except Exception as e:
            print ("add area failed!!!")
            driver.get_screenshot_as_file(".\screenshot\AREA\\001\error_area_add1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add area failed')

    def test_002_area_edit(self):
        make_path.make_path('./screenshot/AREA/002')
        driver = self.driver
        success = 0
        try:
            print (u"""编辑区域对象""")
            login.login(self)

            match_1=0
            match_2=0

            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 区域
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="area"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="area"]/div[1]'))).click()
            time.sleep(1)
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="area_test":
                        match_1=1
                        output.click()
                        break
            if (not match_1):
                print ("No area object founded!")
                success = 0
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'editRegionBtn'))).click()
                wait.until(EC.element_to_be_clickable((By.ID, 'regionShare1'))).click()
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="regionForm"]/div[1]/table/tbody/tr[3]/td[2]/span[1]/textarea')))
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="regionForm"]/div[1]/table/tbody/tr[3]/td[2]/span[1]/textarea'))).clear()
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="regionForm"]/div[1]/table/tbody/tr[3]/td[2]/span[1]/textarea'))).send_keys('Edited')
                driver.find_element_by_id('addRegion').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addRegionBtn')))
            outputs2 = driver.find_elements_by_tag_name('td')
            for output2 in outputs2:
                if output2.get_attribute('field') =='name':
                    text=output2.text
                    if text=="area_test":
                        match_2=1
                        break
            if (not match_2):
                print ("Edit area Failed!")
                driver.get_screenshot_as_file(".\screenshot\AREA\\002\error_area_edit.png")
                success = 0
            else:
                print ("Edit area successfully!!!")
                success = 1

        except Exception as e:
            print ("Edit area failed!!!")
            driver.get_screenshot_as_file(".\screenshot\AREA\\002\error_area_edit1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit area failed')

    def test_003_delete_area(self):
        make_path.make_path('./screenshot/AREA/003')
        driver = self.driver
        success = 0
        try:
            print (u"""删除区域对象""")
            login.login(self)

            match_1=0
            match_2=0

            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 区域
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="area"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="area"]/div[1]'))).click()
            time.sleep(1)
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="area_test":
                        match_1=1
                        output.click()
                        break
            if (not match_1):
                print ("No area object founded!")
                success = 0
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteRegionBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'addRegionBtn')))
            outputs2 = driver.find_elements_by_tag_name('td')
            for output2 in outputs2:
                if output2.get_attribute('field') =='name':
                    text=output2.text
                    if text=="area_test":
                        match_2=1
                        break

            if (match_1 and not match_2):
                print ("Delete area successfully!")
                success = 1
            else:
                print ("Delete area failed!!!")
                driver.get_screenshot_as_file(".\screenshot\AREA\\003\error_area_delete.png")
                success = 0

        except Exception as e:
            print ("Delete area failed!!!")
            driver.get_screenshot_as_file(".\screenshot\AREA\\003\error_area_delete1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete area failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

