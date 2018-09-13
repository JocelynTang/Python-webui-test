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


class SERVER(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/SERVER')

    def test_001_add_server(self):
        make_path.make_path('./screenshot/SERVER/001')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加服务器对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务器
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="server"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="serverFrom"]/table/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("server_1")
            driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[2]/td[2]/span/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('10.10.10.10')
            driver.find_element_by_id('submitBtn').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="server_1":
                        match = 1
                        break
            if (not match):
                print ("Add server failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\001\error_add_server.png")
            else:
                print ("Add server successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\001\error_add_server1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add server failed')

    def test_002_edit_server(self):
        make_path.make_path('./screenshot/SERVER/002')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""修改服务器对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务器
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="server"]/div[1]'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="server_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No server founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\002\error_edit_server.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="serverFrom"]/table/tbody/tr[2]/td[2]/span/input[1]')))
                driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[2]/td[2]/span/input[1]').clear()
                driver.find_element_by_xpath('//*[@id="serverFrom"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('20.20.20.20')
                driver.find_element_by_id('submitBtn').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="server_1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit server failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\002\error_edit_server.png")
            else:
                print ("Edit server successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\002\error_edit_server1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit server failed')

    def test_006_delete_server(self):
        make_path.make_path('./screenshot/SERVER/006')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""删除服务器对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务器
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="server"]/div[1]'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="server_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No server founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\006\error_delete_server.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="server_1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete server successfully!!!")
                success = 1
            else:
                print ("Delete server failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\006\error_delete_server.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\006\error_delete_server1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete server failed')

    def test_003_add_load_balance(self):
        make_path.make_path('./screenshot/SERVER/003')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加负载均衡对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 负载均衡
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="virtual_server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="virtual_server"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBalanceBtn'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="balanceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="balanceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="balanceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("balance_1")
            driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option').click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('wlc').click()# 加权最少连接
            driver.find_element_by_id('balanceSubmit').click()
            time.sleep(3)
            match = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addBalanceBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="balance_1":
                        match = 1
                        break
            if (not match):
                print ("Add load balance failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\003\error_add_load_balance.png")
            else:
                print ("Add load balance successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\003\error_add_load_balance1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add load balance failed')

    def test_004_edit_load_balance(self):
        make_path.make_path('./screenshot/SERVER/004')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""编辑负载均衡对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 负载均衡
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="virtual_server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="virtual_server"]/div[1]'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text=input.text
                    if text=="balance_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No load balance founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\004\error_edit_load_balance.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBalanceBtn'))).click()
                time.sleep(1)
                # 轮流
                wait.until(EC.element_to_be_clickable((By.ID, 'rr'))).click()
                driver.find_element_by_id('balanceSubmit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBalanceBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') == 'name':
                    text=output.text
                    if text=="balance_1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit load balance failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\004\error_edit_load_balance.png")
            else:
                print ("Edit load balance successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\004\error_edit_load_balance1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit load balance failed')

    def test_005_delete_load_balance(self):
        make_path.make_path('./screenshot/SERVER/005')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""删除负载均衡对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 负载均衡
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="virtual_server"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="virtual_server"]/div[1]'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text=input.text
                    if text=="balance_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No load balance founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\005\error_delete_load_balance.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteBalanceBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBalanceBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="balance_1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete load balance successfully!!!")
                success = 1
            else:
                print ("Delete load balance failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVER\\005\error_delete_load_balance.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVER\\005\error_delete_load_balance1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete load balance failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

