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


class VLAN(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/VLAN')

    def test_001_add_single_vlan(self):
        make_path.make_path('./screenshot/VLAN/001')
        driver = self.driver
        success = 0
        try:
            print (u"""添加单个VLAN""")
            login.login(self)
            wait=WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlanAddWindow"]/div/input[1]')))
            driver.find_element_by_xpath('//*[@id="vlanAddForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys('1')
            driver.find_element_by_xpath('//*[@id="vlanAddWindow"]/div/input[1]').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='vlanid':
                    if input.text=='vlan.0001':
                        match = 1
                        time.sleep(5)
                        break

            if (not match):
                print ("Add single vlan failed !!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\001\error_add_single_vlan.png")
            else:
                print ("Add single vlan successfully !!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\001\error_add_single_vlan_1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add single vlan failed')

    def test_002_add_vlan_range(self):
        make_path.make_path('./screenshot/VLAN/002')
        driver = self.driver
        success = 0
        try:
            print (u"添加vlan（范围）")
            i=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="vlanAddForm"]/table/tbody/tr[2]/td[1]/input'))).click()
            driver.find_element_by_xpath('//*[@id="vlanAddForm"]/table/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('1')
            driver.find_element_by_xpath('//*[@id="vlanAddForm"]/table/tbody/tr[2]/td[2]/span[2]/input[1]').send_keys('5')
            driver.find_element_by_xpath('//*[@id="vlanAddWindow"]/div/input[1]').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='ck':
                    i = i+1
            time.sleep(1)
            if i==6:
                print ('add vlan range successfully')
                success =1
            else:
                print ('add vlan range failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\VLAN\\002\error_add_vlan_range.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\002\error_add_vlan_range_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add vlan range failed')

    def test_003_edit_vlan(self):
        make_path.make_path('./screenshot/VLAN/003')
        driver = self.driver
        success = 0
        try:
            print (u"编辑vlan")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0001':
                        match_1 = 1
                        input.click()
                        break

            if (not match_1):
                print ("cann't find vlan.0001")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\003\error_edit_vlan.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="easytabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('100.100.2.2')
                driver.find_element_by_xpath('//*[@id="easytabs"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.255.0.0')
                driver.find_element_by_id('add4Cid').click()
                driver.find_element_by_xpath('//*[@id="vlanEditForm"]/div[3]/input[1]').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            ips = driver.find_elements_by_tag_name('td')
            for ip in ips:
                if ip.get_attribute('field')=='ip':
                    text=ip.text
                    if text=='IPv4:100.100.2.2/255.255.0.0':
                        match_2=1
                        break
            if(match_1 and match_2):
                print ('edit vlan.0001 successfully')
                success = 1
            else:
                print ('edit vlan.0001 failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\003\error_edit_vlan.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\003\error_edit_vlan_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='edit vlan failed')

    def test_004_delete_single_vlan(self):
        make_path.make_path('./screenshot/VLAN/004')
        driver = self.driver
        success = 0
        try:
            print (u"删除单个vlan")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0005':
                        match_1 = 1
                        input.click()
                        time.sleep(1)
                        break

            if (not match_1):
                print ("cann't find vlan.0001")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\004\error_delete_single_vlan.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0005':
                        match_2 = 1
                        input.click()
                        break
            if(match_1 and not match_2):
                print ('delete single vlan successfully')
                success = 1
            else:
                print ('delete single vlan failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\004\error_delete_single_vlan_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\004\error_delete_single_vlan_2.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete single vlan failed')

    def test_005_delete_vlan_range(self):
        make_path.make_path('./screenshot/VLAN/005')
        driver = self.driver
        success = 0
        try:
            print (u"删除vlan（范围）")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            i=0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0002':
                        i = i + 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0003':
                        i = i + 1
                        break
            if i==2:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteRangeBtn'))).click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="vlanDelRangeForm"]/table/tbody/tr/td[2]/span[1]/input[1]').send_keys('2')
                driver.find_element_by_xpath('//*[@id="vlanDelRangeForm"]/table/tbody/tr/td[2]/span[2]/input[1]').send_keys('3')
                driver.find_element_by_xpath('//*[@id="vlanDelRangeForm"]/div/input[1]').click()
                time.sleep(3)
            else:
                print ('cant find vlan')
                success = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            j=i
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0002':
                        j = j - 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text == 'vlan.0003':
                        j = j - 1
                        break
            if i==j:
                print ('delete vlan range successfully')
                success = 1
            else:
                print ('delete vlan range failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\005\error_delete_vlan_range.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\005\error_delete_vlan_range_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete vlan range failed')

    def test_006_clear_vlan(self):
        make_path.make_path('./screenshot/VLAN/006')
        driver = self.driver
        success = 0
        try:
            print (u"清空vlan")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vlan"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'clearBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match=0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vlanid':
                    if input.text=='vlan.0001' or input.text=='vlan.0002' or input.text=='vlan.0003' or input.text=='vlan.0004' or input.text=='vlan.0005':
                        match=1
                        break
            if(not match):
                print ('clear vlan successfully')
                success = 1
            else:
                print ('clear vlan failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VLAN\\006\error_clear_vlan.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VLAN\\006\error_clear_vlan_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='clear vlan failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
