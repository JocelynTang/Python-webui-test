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


class ADDRESS(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        # 创建目录，存放截图
        make_path.make_path('./screenshot/ADRESS')

    def test_001_add_addr(self):
        success = 0
        make_path.make_path('./screenshot/ADRESS/001')
        driver = self.driver
        try:
            print (u"添加地址对象")
            time.sleep(1)
            login.login(self)

            match = 0
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
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            # 名称
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="addrForm"]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]'))).send_keys("addr1")
            # 子网
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="typeSubnet"]'))).click()
            # IP
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="addr3"]/td/span[1]/input[1]'))).send_keys("3.3.3.0")
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="addr3"]/td/span[2]/input[1]'))).send_keys("24")
            wait.until(EC.element_to_be_clickable((By.ID, 'submitAddress'))).click()
            time.sleep(4)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            # 确认地址对象是否添加成功
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="addr1":
                        match = 1
                        break
            if not match:
                print ("Add address failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\001\error_add_address.png")
            else:
                print ("Add address successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\001\error_add_addr1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add address failed')

    def test_002_addr_edit(self):
        make_path.make_path('./screenshot/ADRESS/002')
        driver = self.driver
        success = 0
        try:
            print (u"""修改地址对象""")

            login.login(self)
            match_1 = 0
            match_2 = 0

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
            inputs1 = driver.find_elements_by_tag_name('td')
            for input1 in inputs1:
                if input1.get_attribute('field') =='name':
                    text=input1.text
                    if text=="addr1":
                        input1.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ("No address founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\002\error_edit_address.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'editBtn'))).click()
                wait.until(EC.element_to_be_clickable((By.ID,'addrshare1'))).click()
                driver.find_element_by_id('submitAddress').click()
                time.sleep(5)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs2 = driver.find_elements_by_tag_name('td')
            for input2 in inputs2:
                if input2.get_attribute('field') =='name':
                    text=input2.text
                    if text=="addr1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit address failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\002\error_edit_address.png")
            else:
                print ("Edit address successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\002\error_edit_addr1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit address failed')

    def test_006_delete_addr(self):
        make_path.make_path('./screenshot/ADRESS/006')
        driver = self.driver
        success = 0
        try:
            print (u"""删除地址对象""")
            login.login(self)
            match_1 = 0
            match_2 = 0

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

            inputs1 = driver.find_elements_by_tag_name('td')
            for input1 in inputs1:
                if input1.get_attribute('field') =='name':
                    text=input1.text
                    if text=="addr1":
                        input1.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ("No address founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\006\error_delete_address.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'deleteBtn'))).click()
                confirm_or_cancel.confirm(self)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn')))
            inputs2 = driver.find_elements_by_tag_name('td')
            for input2 in inputs2:
                if input2.get_attribute('field') =='name':
                    text=input2.text
                    if text=="addr1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete address successfully!!!")
                success = 1
            else:
                print ("Delete address failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\006\error_delete_address.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\006\error_delete_addr1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete address failed')

    def test_003_add_addrgroup(self):
        make_path.make_path('./screenshot/ADRESS/003')
        driver = self.driver
        success = 0
        try:
            print (u"""添加地址组对象""")
            login.login(self)

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
            # 地址组
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang') == 'ADDR_GROUP':
                    name.click()
                    break
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH,
                        '//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]'))).send_keys("addr_group1")
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftSelectItemCid"]/option'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupLeft'))).click()
            driver.find_element_by_id("addAddrGro").click()
            time.sleep(4)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="addr_group1":
                        match = 1
                        break
            if (not match):
                print ("Add address group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\003\error_add_addressgroup.png")
            else:
                print ("Add address group successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\003\error_add_addr_group1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add addr group failed')

    def test_004_addrgroup_edit(self):
        make_path.make_path('./screenshot/ADRESS/004')
        driver = self.driver
        success = 0
        try:
            print (u"""修改地址组对象""")
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
            # 地址
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(1)
            # 地址组
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang')=='ADDR_GROUP':
                    name.click()
                    break
            time.sleep(2)
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="addr_group1":
                        input.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ("No address group founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\004\error_add_addressgroup.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'editBtn'))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rightSelectItemCid"]/option'))).click()
                wait.until(EC.element_to_be_clickable((By.ID,'addrgroupRight'))).click()
                driver.find_element_by_id("addAddrGro").click()
                time.sleep(4)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="addr_group1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit address group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\004\error_edit_addressgroup.png")
            else:
                print ("Edit address group successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\004\error_edit_addr_group1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit addr group failed')

    def test_005_delete_addrgroup(self):
        make_path.make_path('./screenshot/ADRESS/005')
        driver = self.driver
        success = 0
        try:
            print (u"""删除地址组对象""")
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
            # 地址
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address"]/div[1]'))).click()
            time.sleep(1)
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang')=='ADDR_GROUP':
                    name.click()
                    break
            time.sleep(2)
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="addr_group1":
                        input.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ("No address group founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\005\error_add_addressgroup.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'deleteBtn'))).click()
                confirm_or_cancel.confirm(self)

            wait.until(EC.element_to_be_clickable((By.ID,'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="addr_group1":
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ("Delete address group successfully!!!")
                success = 1
            else:
                print ("Delete address group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADRESS\\005\error_delete_addressgroup.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADRESS\\005\error_delete_addr_group1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete addr group failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

