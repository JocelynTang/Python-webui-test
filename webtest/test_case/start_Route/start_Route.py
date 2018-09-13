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


class ROUTE(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/ROUTE')

    def test_001_add_staticroute(self):
        make_path.make_path('./screenshot/ROUTE/001')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加静态路由""")
            login.login(self)
            wait=WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID,'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="route"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="staticRoute"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'staticRouteAdd'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,'//*[@id="staticRouteAddForm"]/table/tbody/tr[2]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="staticRouteAddForm"]/table/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('10.1.1.0')
            driver.find_element_by_xpath('//*[@id="staticRouteAddForm"]/table/tbody/tr[2]/td[2]/span[2]/input[1]').send_keys('24')
            driver.find_element_by_xpath('//*[@id="staticRouteAddForm"]/table/tbody/tr[3]/td[2]/div/span/input[1]').send_keys('20.1.1.1')
            driver.find_element_by_id('staticRouteSubmit').click()
            time.sleep(3)
            match = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'staticRouteAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'dst':
                    text = input.text
                    if text == "10.1.1.0/24":
                        match = 1
                        break
            if (not match):
                print ("Add static route failed !!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\001\error_add_static_route.png")
            else:
                print ("Add static route successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ROUTE\\001\error_add_staticroute1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add static route failed')

    def test_002_delete_static_route(self):
        make_path.make_path('./screenshot/ROUTE/002')
        driver = self.driver
        success = 0
        try:
            print (u"""删除静态路由""")
            match_1 = 0
            match_2 = 0
            time.sleep(1)
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="route"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="staticRoute"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'staticRouteAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'dst':
                    text = input.text
                    if text == "10.1.1.0/24":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("no static route founded !!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\002\error_delete_static_route.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'staticRouteDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'staticRouteAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'dst':
                    text = input.text
                    if text == "10.1.1.0/24":
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ('delete static route successfully')
                success = 1
            else:
                print ('delete static route failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\002\error_delete_static_route_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ROUTE\\002\error_delete_static_route_2.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete static route failed')

    def test_003_add_policy_route(self):
        make_path.make_path('./screenshot/ROUTE/003')
        driver = self.driver
        time.sleep(1)
        success = 0
        try:
            print (u"""添加策略路由""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="route"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="policyRoute"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteAdd'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="policyRouteAddForm"]/table/tbody/tr[2]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('10.10.10.0/24')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[3]/td[2]/span/input[1]').send_keys('20.20.20.0/24')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[4]/td[2]/span[1]/input[1]').send_keys('22')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').send_keys('33')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[6]/td[2]/span/input[1]').send_keys('TCP')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[7]/td[2]/div/span/input[1]').send_keys('10.10.10.111')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[11]/td[2]/span[1]/input[1]').send_keys('11')
            driver.find_element_by_xpath('//*[@id="policyRouteAddForm"]/table/tbody/tr[12]/td[2]/span[1]/input[1]').send_keys('22')
            driver.find_element_by_id('policyRouteSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteAdd')))
            i = 0
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='ck':
                    i = i+1
            time.sleep(1)
            if i==2:
                print ('add policy route successfully')
                success = 1
            else:
                print ('add policy route failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\003\error_add_policy_route.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ROUTE\\003\error_add_policy_route_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add policy route failed')

    def test_004_edit_policy_route(self):
        make_path.make_path('./screenshot/ROUTE/004')
        driver = self.driver
        success = 0
        try:
            print (u"""修改策略路由""")
            match_1 =0
            match_2 =0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="route"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="policyRoute"]/div[1]'))).click()
            time.sleep(1)
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='weight':
                    text=input.text
                    if text=='22':
                        input.click()
                        match_1=1
                        break
            if(not match_1):
                print ('cant find policy route')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\error_edit_policy_route.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteEdit'))).click()
                time.sleep(1)
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="policyRouteEditForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]')))
                driver.find_element_by_xpath('//*[@id="policyRouteEditForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').clear()
                driver.find_element_by_xpath('//*[@id="policyRouteEditForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').send_keys('1')
                driver.find_element_by_id('policyRouteEditSubmit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'weight':
                    text = input.text
                    if text == '1':
                        match_2 = 1
                        break
            if(match_1 and match_2):
                print ('edit policy route successfully')
                success = 1
            else:
                print ('edit policy route failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\004\error_edit_policy_route_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ROUTE\\004\error_edit_policy_route_2.png")
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='edit policy route failed')

    def test_005_delete_route_policy(self):
        make_path.make_path('./screenshot/ROUTE/005')
        driver = self.driver
        success = 0
        try:
            print (u"""删除策略路由""")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="route"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="policyRoute"]/div[1]'))).click()
            time.sleep(1)
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='weight':
                    text=input.text
                    if text=='1':
                        input.click()
                        match_1=1
                        break
            if(not match_1):
                print ('cant find policy route')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\005\error_delete_policy_route.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'policyRouteAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'weight':
                    text = input.text
                    if text == '1':
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ('delete policy route successfully')
                success = 1
            else:
                print ('delete policy route failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ROUTE\\005\error_delete_policy_route_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ROUTE\\005\error_delete_policy_route_2.png")
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete policy route failed')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
