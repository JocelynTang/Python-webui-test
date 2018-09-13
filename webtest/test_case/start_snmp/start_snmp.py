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


class SNMP(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/SNMP')

    def test_001_add_snmp_manage(self):
        make_path.make_path('./screenshot/SNMP/001')
        driver = self.driver
        success = 0
        try:
            print (u"""添加SNMP管理主机""")
            login.login(self)
            wait=WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'shutdownDisable')))
            driver.find_element_by_xpath('//*[@id="addhost1Form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys("host1")
            driver.find_element_by_id('shutdownDisable').click()
            driver.find_element_by_xpath('//*[@id="sp2"]/span[1]/input[1]').send_keys('116.1.1.0')
            driver.find_element_by_xpath('//*[@id="sp2"]/span[2]/input[1]').send_keys('24')
            driver.find_element_by_xpath('//*[@id="addhost1Form"]/table/tbody/tr[4]/td[2]/span/input[1]').send_keys('public')
            driver.find_element_by_id('addSnmpManageHost').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="host1":
                        match = 1
                        break
            if (not match):
                print ("Add snmp manage failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\001\error_add_snmp_manage.png")
            else:
                success = 1
                print ("Add snmp manage successfully!!!")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\001\error_add_snmp_manage1.png")
            success = 0
            print('error:',e)

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add snmp manage failed')

    def test_002_add_snmp_trap(self):
        make_path.make_path('./screenshot/SNMP/002')
        driver = self.driver
        success = 0
        try:
            print (u"""添加SNMP陷阱主机""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[2]'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'addTraBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addSnmpHost')))
            driver.find_element_by_xpath('//*[@id="addhost2Form"]/table/tbody/tr[1]/td[2]/span/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="addhost2Form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys("traphost1")
            driver.find_element_by_xpath('//*[@id="addhost2Form"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('116.116.116.116')
            driver.find_element_by_id('addSnmpHost').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addTraBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="traphost1":
                        match = 1
                        break
            if (not match):
                print ("Add snmp trap failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\002\error_add_snmp_trap.png")
            else:
                print ("Add snmp trap successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\002\error_add_snmp_trap1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add snmp trap failed')

    def test_003_add_snmp_V3(self):
        make_path.make_path('./screenshot/SNMP/003')
        driver = self.driver
        success = 0
        try:
            print (u"""添加SNMPV3用户""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            buttons = driver.find_elements_by_tag_name('a')
            for button in buttons:
                if button.get_attribute('lang') == "SNMP_V3_USER":
                    button.click()
                    time.sleep(1)
                    break
            wait.until(EC.element_to_be_clickable((By.ID, 'addVBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'SNMPV3')))
            driver.find_element_by_xpath('//*[@id="addhost3Form"]/table/tbody/tr[1]/td[2]/span/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="addhost3Form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys("snmpV31")
            driver.find_element_by_xpath('//*[@id="addhost3Form"]/table/tbody/tr[3]/td[2]/span[1]/input[1]').send_keys('talent12')
            driver.find_element_by_xpath('//*[@id="sp3"]/td[2]/span[1]/input[1]').send_keys('superman')
            driver.find_element_by_id('SNMPV3').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='user_name':
                    text=input.text
                    if text=="snmpV31":
                        match = 1
                        break
            if (not match):
                print ("Add snmp V3 failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\003\error_add_snmp_V3.png")
            else:
                print ("Add snmp V3 successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\003\error_add_snmp_V31.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add snmpV3 failed')

    def test_004_start_snmp(self):
        make_path.make_path('./screenshot/SNMP/004')
        driver = self.driver
        success = 0
        try:
            print (u"启动snmp服务")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            driver.find_element_by_id('btnApp').click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'btnStart'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            text=driver.find_element_by_id('btnStart').get_attribute('disabled')
            if text:
                print ('start snmp successfully')
                success = 1
            else:
                print ('start snmp failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\SNMP\\004\error_start_snmp.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\004\error_start_snmp_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='start snmp failed')

    def test_005_stop_snmp(self):
        make_path.make_path('./screenshot/SNMP/005')
        driver = self.driver
        success = 0
        try:
            print (u"停止snmp服务")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'btnStop'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            text = driver.find_element_by_id('btnStop').get_attribute('disabled')
            if text:
                print ('stop snmp successfully')
                success = 1
            else:
                print ('stop snmp failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\SNMP\\005\error_stop_snmp.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\005\error_stop_snmp_1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='stop snmp failed')

    def test_006_delete_snmp_manage(self):
        make_path.make_path('./screenshot/SNMP/006')
        driver = self.driver
        success = 0
        try:
            print (u"删除snmp管理主机")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="host1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("no snmp manage founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\006\error_delete_snmp_manage.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == "host1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ('delete snmp manage successfully')
                success = 1
            else:
                print ('delete snmp manage failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\006\error_delete_snmp_manage_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\006\error_delete_snmp_manage_2.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete snmp manage failed')

    def test_007_delete_snmp_trap(self):
        make_path.make_path('./screenshot/SNMP/007')
        driver = self.driver
        success = 0
        try:
            print (u"删除snmp陷阱主机")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[2]'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'addTraBtn')))
            match_1 = 0
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="traphost1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("no snmp trap founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\007\error_delete_snmp_trap.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteTraBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addTraBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == "traphost1":
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ('delete snmp trap successfully')
                success = 1
            else:
                print ('delete snmp trap failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\007\error_delete_snmp_trap_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\007\error_delete_snmp_trap_2.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete snmp trap failed')

    def test_008_delete_snmp_V3(self):
        make_path.make_path('./screenshot/SNMP/008')
        driver = self.driver
        success = 0
        try:
            print (u"删除snmpv3用户")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snmp"]/div[1]'))).click()
            time.sleep(1)
            buttons = driver.find_elements_by_tag_name('a')
            for button in buttons:
                if button.get_attribute('lang') == "SNMP_V3_USER":
                    button.click()
                    time.sleep(2)
                    break
            match_1 = 0
            match_2 = 0
            wait.until(EC.element_to_be_clickable((By.ID, 'addVBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='user_name':
                    text=input.text
                    if text=="snmpV31":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("no snmp V3 founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\008\error_delete_snmp_V3.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteVBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'user_name':
                    text = input.text
                    if text == "snmpV31":
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ('delete snmp V3 successfully')
                success = 1
            else:
                print ('delete snmp V3 failed')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SNMP\\008\error_delete_snmp_V3_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\SNMP\\008\error_delete_snmp_V3_2.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete snmp V3 failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()


