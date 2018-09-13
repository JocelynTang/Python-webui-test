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


class INTERFACE(unittest.TestCase):
    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/INTERFACE')
        file = '.\config\interface.json'
        with open(file, 'r') as a:
            b = json.load(a)
            self.inf1 = str(b['inf1'])
            self.inf2 = str(b['inf2'])
            self.inf3 = str(b['inf3'])

    def test_001_edit_interface(self):
        make_path.make_path('./screenshot/INTERFACE/001')
        driver = self.driver
        success = 0
        try:
            print(u"编辑物理接口")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(3)
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'interface_name':
                    text = input.text
                    if text == self.inf1:
                        input.click()
                        break
            # 添加ip
            wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.ID, 'submitBtn')))
            driver.find_element_by_xpath(
                '//*[@id="tabsChange"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('1.1.1.1')
            driver.find_element_by_xpath(
                '//*[@id="tabsChange"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.0.0.0')
            driver.find_element_by_id('add4Cid').click()
            driver.find_element_by_id('submitBtn').click()
            time.sleep(5)
            match_1 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'ip':
                    text = input.text
                    if text == 'IPv4:1.1.1.1/255.0.0.0':
                        match_1 = 1
                        break
            # 删除ip
            if match_1:
                inputs = driver.find_elements_by_tag_name('td')
                for input in inputs:
                    if input.get_attribute('field') == 'interface_name':
                        text = input.text
                        if text == self.inf1:
                            input.click()
                            break
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(3)
                wait.until(EC.presence_of_element_located((By.ID, 'submitBtn')))
                driver.find_element_by_name('ck').click()
                driver.find_element_by_id('delIpv4').click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                wait.until(EC.presence_of_element_located((By.ID, 'submitBtn'))).click()
                time.sleep(5)
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'ip':
                    text = input.text
                    if text == 'IPv4:1.1.1.1/255.0.0.0':
                        match_2 = 1
                        break
            if match_1 and not match_2:
                success = 1
            else:
                success = 0
                driver.get_screenshot_as_file('./screenshot/INTERFACE/001/error_edit_interface1.png')

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/001/error_edit_interface2.png')
            print('error:',e)
        finally:
            self.assertTrue(success, msg='edit interface failed')
            logout.logout(self)

    def test_002_add_virtual_line(self):
        make_path.make_path('./screenshot/INTERFACE/002')
        driver = self.driver
        success = 0
        try:
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[4]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'virtualLineSubmit')))
            driver.find_element_by_xpath('//*[@id="virtualAddFrom"]/table/tbody/tr[1]/td[2]/span/span').click()
            time.sleep(1)
            infs = driver.find_elements_by_tag_name('div')
            for inf in infs:
                if inf.get_attribute('class') == 'combobox-item':
                    text = inf.text
                    if text == self.inf2:
                        inf.click()
                        break
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="virtualAddFrom"]/table/tbody/tr[2]/td[2]/span/span').click()
            time.sleep(1)
            infs = driver.find_elements_by_tag_name('div')
            for inf in infs:
                if inf.get_attribute('class') == 'combobox-item':
                    text = inf.text
                    if text == self.inf3:
                        inf.click()
                        break
            driver.find_element_by_id('virtualLineSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            match_2 = 0
            infs = driver.find_elements_by_tag_name('td')
            for inf in infs:
                if inf.get_attribute('field') == 'dev':
                    text = inf.text
                    if text == self.inf2:
                        match_1 = 1
                        break
            infs = driver.find_elements_by_tag_name('td')
            for inf in infs:
                if inf.get_attribute('field') == 'peer_dev':
                    text = inf.text
                    if text == self.inf3:
                        match_2 = 1
                        break
            if match_1 and match_2:
                success = 1
            else:
                success = 0
                driver.get_screenshot_as_file('./screenshot/INTERFACE/002/error_add_virtual_line1.png')

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/002/error_add_virtual_line2.png')
            print('error:', e)
        finally:
            self.assertTrue(success, msg='add virtual line failed')
            logout.logout(self)

    def test_003_delete_virtual_line(self):
        make_path.make_path('./screenshot/INTERFACE/003')
        driver = self.driver
        success = 0
        try:
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[4]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            driver.find_element_by_name('ck').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'delBtn'))).click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            match_2 = 0
            infs = driver.find_elements_by_tag_name('td')
            for inf in infs:
                if inf.get_attribute('field') == 'dev':
                    text = inf.text
                    if text == self.inf2:
                        match_1 = 1
                        break
            infs = driver.find_elements_by_tag_name('td')
            for inf in infs:
                if inf.get_attribute('field') == 'peer_dev':
                    text = inf.text
                    if text == self.inf3:
                        match_2 = 1
                        break
            if not match_1 and not match_2:
                success = 1
            else:
                success = 0
                driver.get_screenshot_as_file('./screenshot/INTERFACE/003/error_delete_virtual_line1.png')

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/003/error_delete_virtual_line2.png')
            print('error:', e)
        finally:
            self.assertTrue(success, msg='delete virtual line failed')
            logout.logout(self)

    def test_004_add_bond(self):
        make_path.make_path('./screenshot/INTERFACE/004')
        driver = self.driver
        success = 0
        try:
            wait = WebDriverWait(driver, 10)
            login.login(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[5]'))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'bondAdd'))).click()
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.ID, 'leftSelectItemCid')))
            # 选择负载均衡算法，bond ID使用默认的ID 0
            driver.find_element_by_xpath('//*[@id="bondAddForm"]/table/tbody/tr[2]/td[2]/span/span').click()
            time.sleep(1)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class')=='combobox-item':
                    text = type.text
                    if text == u'根据源mac地址均衡':
                        type.click()
                        break
            # 手工模式
            wait.until(EC.element_to_be_clickable((By.ID, 'commHandmadeCid'))).click()
            # 选择接口
            infs = driver.find_elements_by_tag_name('option')
            for inf in infs:
                if inf.get_attribute('value')==self.inf1:
                    inf.click()
                    break
            # driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option[2]').click()
            driver.find_element_by_id('addrgroupLeft').click()
            infs = driver.find_elements_by_tag_name('option')
            for inf in infs:
                if inf.get_attribute('value') == self.inf2:
                    inf.click()
                    break
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('bondAddSubmit').click()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.NAME, 'ck')))
            match = 0
            targets = driver.find_elements_by_tag_name('td')
            for target in targets:
                if target.get_attribute('field') == 'bond_name':
                    text = target.text
                    if text == 'bond0':
                        match = 1
                        break
            if match:
                success = 1
            else:
                success=0
                print('add bond failed')
                driver.get_screenshot_as_file('./screenshot/INTERFACE/004/error_add_bond1.png')

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/004/error_add_bond2.png')
            print('error:', e)
        finally:
            self.assertTrue(success, msg='add bond failed')
            logout.logout(self)

    def test_005_edit_bond(self):
        make_path.make_path('./screenshot/INTERFACE/005')
        driver = self.driver
        success = 0
        try:
            wait = WebDriverWait(driver, 10)
            login.login(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[5]'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'bondClear')))
            match_1 = 0
            targets = driver.find_elements_by_tag_name('td')
            for target in targets:
                if target.get_attribute('field') == 'bond_name':
                    text = target.text
                    if text == 'bond0':
                        match_1 = 1
                        target.click()
                        break
            if match_1:
                wait.until(EC.element_to_be_clickable((By.ID, 'bondAttr'))).click()
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, 'bondDetailSubmit')))
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('2.2.2.2')
                driver.find_element_by_xpath('//*[@id="easyTabs"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.0.0.0')
                driver.find_element_by_id('add4Cid').click()
                driver.find_element_by_id('bondDetailSubmit').click()
                time.sleep(3)
            else:
                success = 0
                print('cannot find bond')
                driver.get_screenshot_as_file('./screenshot/INTERFACE/005/error_edit_bond.png')
            wait.until(EC.element_to_be_clickable((By.ID, 'bondClear')))
            match_2 = 0
            targets = driver.find_elements_by_tag_name('td')
            for target in targets:
                if target.get_attribute('field') == 'ip':
                    text = target.text
                    if text == 'IPv4:2.2.2.2/255.0.0.0':
                        match_2 = 1
                        break
            if match_2:
                success = 1
            else:
                success = 0
                print('edit bond failed')
                driver.get_screenshot_as_file('./screenshot/INTERFACE/005/error_edit_bond1.png')

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/005/error_edit_bond2.png')
            print('error:', e)
        finally:
            self.assertTrue(success, msg='edit bond failed')
            logout.logout(self)

    def test_006_delete_bond(self):
        make_path.make_path('./screenshot/INTERFACE/006')
        driver = self.driver
        success = 0
        try:
            wait = WebDriverWait(driver, 10)
            login.login(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[5]'))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'bondClear')))
            match_1 = 0
            targets = driver.find_elements_by_tag_name('td')
            for target in targets:
                if target.get_attribute('field') == 'bond_name':
                    text = target.text
                    if text == 'bond0':
                        match_1 = 1
                        target.click()
                        break
            if match_1:
                wait.until(EC.element_to_be_clickable((By.ID, 'bondDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            else:
                success = 0
                print('cannot find bond')
                driver.get_screenshot_as_file('./screenshot/INTERFACE/006/error_delete_bond.png')
            wait.until(EC.element_to_be_clickable((By.ID, 'bondClear')))
            match_2 = 0
            targets = driver.find_elements_by_tag_name('td')
            for target in targets:
                if target.get_attribute('field') == 'bond_name':
                    text = target.text
                    if text == 'bond0':
                        match_2 = 1
                        break
            if match_2:
                success = 0
                print('delete bond failed')
                driver.get_screenshot_as_file('./screenshot/INTERFACE/006/error_delete_bond1.png')
            else:
                success = 1

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file('./screenshot/INTERFACE/006/error_delete_bond2.png')
            print('error:', e)
        finally:
            self.assertTrue(success, msg='delete bond failed')
            logout.logout(self)


    def tearDown(self):
        self.driver.quit()