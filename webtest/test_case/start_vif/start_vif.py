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


class VIF(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/VIF')
        file = '.\config\interface.json'
        with open(file, 'r') as a:
            b = json.load(a)
            self.inf1 = str(b['inf1'])
            self.inf2 = str(b['inf2'])
            self.inf3 = str(b['inf3'])

    def test_001_add_macvif(self):
        make_path.make_path('./screenshot/VIF/001')
        driver = self.driver
        success = 0
        try:
            print (u"添加MAC子接口")
            match = 0
            login.login(self)
            wait=WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'singleCid'))).click()
            driver.find_element_by_xpath('//*[@id="macvifAddForm"]/table/tbody/tr[1]/td[2]/span/span').click()
            time.sleep(1)
            infs = driver.find_elements_by_tag_name('div')
            for inf in infs:
                if inf.get_attribute('class') == 'combobox-item':
                    text = inf.text
                    if text == self.inf1:
                        inf.click()
                        time.sleep(1)
                        break
            driver.find_element_by_xpath('//*[@id="macvifAddForm"]/table/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('1')
            driver.find_element_by_id('macvifSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='interface_name':
                    text_1=input.text
                    if text_1 == self.inf1 + 'mv01':
                        match = 1
                        break
            if(match):
                print ('add macvif successfully!!!')
                success = 1
            else:
                print ('add macvif failed!!!')
                driver.get_screenshot_as_file(".\screenshot\VIF\\001\error_add_macvif.png")
                success = 0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\001\error_add_macvif1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Add macvif failed!!!')

    def test_002_edit_macvif(self):
        make_path.make_path('./screenshot/VIF/002')
        driver = self.driver
        success = 0
        try:
            print (u"编辑MAC子接口")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'interface_name':
                    text_1 = input_1.text
                    if text_1 ==  self.inf1 + 'mv01':
                        input_1.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ('no macvif founded!!!')
                success = 0
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'macvifEdit'))).click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('116.116.11.6')
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.255.0.0')
                driver.find_element_by_id('ha4Cid').click()
                driver.find_element_by_id('add4Cid').click()
                driver.find_element_by_id('macvifEditSubmit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd')))
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') == 'ip':
                    text_2 = input_2.text
                    if text_2 == 'IPv4:116.116.11.6/255.255.0.0':
                        match_2 = 1
                        break
            if match_2:
                print ('edit macvif successfully!!!')
                success = 1
            else:
                print ('edit macvif failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VIF\\002\error_edit_macvif.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\002\error_edit_macvif1.png")
            print('error:',e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'Edit macvif failed!!!')

    def test_003_delete_macvif(self):
        make_path.make_path('./screenshot/VIF/003')
        driver = self.driver
        success = 0
        try:
            print (u"删除MAC子接口")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'interface_name':
                    text_1 = input_1.text
                    if text_1 ==  self.inf1 + 'mv01':
                        match_1 = 1
                        break
            if (not match_1):
                print ('no macvif founded!!!')
                success = 0
            else:
                driver.find_element_by_name('ck').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'macvifDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'macvifAdd')))
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') == 'interface_name':
                    text_2 = input_2.text
                    if text_2 ==  self.inf1 + 'mv01':
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ('delete macvif successfully!!!')
                success = 1
            else:
                print ('delete macvif failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VIF\\003\error_delete_macvif.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\003\error_delete_macvif1.png")
            print('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Delete macvif failed!!!')

    def test_004_add_tagvif(self):
        make_path.make_path('./screenshot/VIF/004')
        driver = self.driver
        success = 0
        try:
            print (u"添加TAG子接口")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tabTwo'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'singleCid'))).click()
            driver.find_element_by_xpath('//*[@id="macvifAddForm"]/table/tbody/tr[1]/td[2]/span/span').click()
            time.sleep(1)
            infs = driver.find_elements_by_tag_name('div')
            for inf in infs:
                if inf.get_attribute('class') == 'combobox-item':
                    text = inf.text
                    if text == self.inf2:
                        inf.click()
                        time.sleep(1)
                        break
            driver.find_element_by_xpath('//*[@id="macvifAddForm"]/table/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('1')
            driver.find_element_by_id('macvifSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='interface_name':
                    text_1=input.text
                    if text_1 == self.inf2 + '.1':
                        match = 1
                        break
            if(match):
                print ('add tagvif successfully!!!')
                success = 1
            else:
                print ('add tagvif failed!!!')
                driver.get_screenshot_as_file(".\screenshot\VIF\\004\error_add_tagvif.png")
                success = 0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\004\error_add_tagvif1.png")
            print('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Add tagvif failed!!!')

    def test_005_edit_tagvif(self):
        make_path.make_path('./screenshot/VIF/005')
        driver = self.driver
        success = 0
        try:
            print (u"修改TAG子接口")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tabTwo'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'interface_name':
                    text_1 = input_1.text
                    if text_1 == self.inf2 + '.1':
                        input_1.click()
                        match_1 = 1
                        break
            if (not match_1):
                print ('no tagvif founded!!!')
                success = 0
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'tagvifEdit'))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]')))
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('116.116.11.6')
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.255.0.0')
                driver.find_element_by_id('ha4Cid').click()
                driver.find_element_by_id('add4Cid').click()
                driver.find_element_by_id('tagvifEditSubmit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd')))
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') == 'ip':
                    text_2 = input_2.text
                    if text_2 == 'IPv4:116.116.11.6/255.255.0.0':
                        match_2 = 1
                        break
            if match_2:
                print ('edit tagvif successfully!!!')
                success = 1
            else:
                print ('edit tagvif failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VIF\\005\error_edit_tagvif.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\005\error_edit_tagvif1.png")
            print('error:',e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'Edit tagvif failed!!!')

    def test_006_delete_tagvif(self):
        make_path.make_path('./screenshot/VIF/006')
        driver = self.driver
        success = 0
        try:
            print (u"删除TAG子接口")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="macvif"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tabTwo'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd')))
            inputs_1 = driver.find_elements_by_tag_name('td')
            for input_1 in inputs_1:
                if input_1.get_attribute('field') == 'interface_name':
                    text_1 = input_1.text
                    if text_1 == self.inf2 + '.1':
                        match_1 = 1
                        break
            if (not match_1):
                print ('no tagvif founded!!!')
                success = 0
            else:
                driver.find_element_by_name('ck').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'tagvifDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'tagvifAdd')))
            inputs_2 = driver.find_elements_by_tag_name('td')
            for input_2 in inputs_2:
                if input_2.get_attribute('field') == 'interface_name':
                    text_2 = input_2.text
                    if text_2 == self.inf2 + '.1':
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ('delete tagvif successfully!!!')
                success = 1
            else:
                print ('delete tagvif failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VIF\\006\error_delete_tagvif.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\VIF\\006\error_delete_tagvif1.png")
            print('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='Delete tagvif failed!!!')

    def tearDown(self):
        driver = self.driver
        driver.quit()

if __name__ == "__main__":
    unittest.main()
