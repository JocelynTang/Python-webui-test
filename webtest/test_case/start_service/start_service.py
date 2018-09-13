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


class SERVICE(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/SERVICE')

    def test_001_add_self_service(self):
        make_path.make_path('./screenshot/SERVICE/001')
        driver = self.driver
        success = 0
        try:
            print (u"""添加自定义服务对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'selfService'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="selfServiceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="selfServiceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="selfServiceForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("selfservice_1")
            driver.find_element_by_id('typeSwitchUdp').click()# udp
            driver.find_element_by_xpath('//*[@id="servTcpUdp"]/td/span[2]/input[1]').send_keys('23')
            driver.find_element_by_xpath('//*[@id="servTcpUdp"]/td/span[3]/input[1]').send_keys('53')
            driver.find_element_by_id('submit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="selfservice_1":
                        match = 1
                        break

            if (not match):
                print ("Add self service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\001\error_add_self_service.png")
            else:
                print ("Add self service successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\001\error_add_self_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add self service failed')

    def test_002_edit_self_service(self):
        make_path.make_path('./screenshot/SERVICE/002')
        driver = self.driver
        success = 0
        try:
            print (u"""编辑自定义服务对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'selfService'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="selfservice_1":
                        match_1 = 1
                        input.click()
                        break

            if (not match_1):
                print ("No self service founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\002\error_edit_self_service.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="selfServiceForm"]/table/tbody/tr[3]/td[2]/span[1]/textarea')))
                driver.find_element_by_xpath('//*[@id="selfServiceForm"]/table/tbody/tr[3]/td[2]/span[1]/textarea').clear()
                driver.find_element_by_xpath('//*[@id="selfServiceForm"]/table/tbody/tr[3]/td[2]/span[1]/textarea').send_keys('editbytql')
                driver.find_element_by_id('typeSwitchTcp').click()# tcp
                driver.find_element_by_id('submit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') == 'name':
                    text=output.text
                    if text=="selfservice_1":
                        match_2 = 1
                        break

            if (not match_2):
                print ("Edit self service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\002\error_edit_self_service.png")
            else:
                print ("Edit self service successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\002\error_edit_self_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit self service failed')

    def test_003_delete_self_service(self):
        make_path.make_path('./screenshot/SERVICE/003')
        driver = self.driver
        success = 0
        try:
            print (u"""删除自定义服务对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'selfService'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text=input.text
                    if text=="selfservice_1":
                        match_1 = 1
                        input.click()
                        break

            if (not match_1):
                print ("No self service founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\003\error_delete_self_service.png")
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
                    if text=="selfservice_1":
                        match_2 = 1
                        break

            if (match_1 and not match_2):
                print ("Delete self service successfully!!!")
                success = 1
            else:
                print ("Delete self service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\003\error_delete_self_service.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\003\error_delete_self_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete self service failed')

    def test_004_add_group_service(self):
        make_path.make_path('./screenshot/SERVICE/004')
        driver = self.driver
        success = 0
        try:
            print (u"""添加服务组对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'groupService'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("groupservice_1")
            driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option[2]').click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('addServGroup').click()
            time.sleep(3)
            match = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="groupservice_1":
                        match = 1
                        break
            if (not match):
                print ("Add group service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\004\error_add_group_service.png")
            else:
                print ("Add group service successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\004\error_add_group_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add group service failed')

    def test_005_edit_group_service(self):
        make_path.make_path('./screenshot/SERVICE/005')
        driver = self.driver
        success = 0
        try:
            print (u"""修改服务组对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'groupService'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="groupservice_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No group service founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\005\error_edit_group_service.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option[3]').click()
                driver.find_element_by_id('addrgroupLeft').click()
                driver.find_element_by_id('addServGroup').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="groupservice_1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit group service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\005\error_edit_group_service.png")
            else:
                print ("Edit group service successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\005\error_edit_group_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit group service failed')

    def test_006_delete_group_service(self):
        make_path.make_path('./screenshot/SERVICE/006')
        driver = self.driver
        success = 0
        try:
            print (u"""删除服务组对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            # 安全策略
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            # 对象
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="object"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            # 服务
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="service"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'groupService'))).click()
            time.sleep(1)
            match_1 = 0
            match_2 = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="groupservice_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No group service founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\006\error_delete_group_service.png")
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
                    if text=="groupservice_1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete group service successfully!!!")
                success = 1
            else:
                print ("Delete group service failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SERVICE\\006\error_delete_group_service.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SERVICE\\006\error_delete_group_service1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete group service failed')

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()

