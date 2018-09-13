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


class VSYS(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/VSYS')
        file = '.\config\interface.json'
        with open(file, 'r') as a:
            b = json.load(a)
            self.inf1 = str(b['inf1'])
            self.inf2 = str(b['inf2'])
            self.inf3 = str(b['inf3'])

    def test_001_add_vsys(self):
        make_path.make_path('./screenshot/VSYS/001')
        driver = self.driver
        success = 0
        try:
            print (u"添加虚系统")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="systemVsys"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="systemVsysForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="systemVsysForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("vsys_1")
            driver.find_element_by_xpath('//*[@id="systemVsysForm"]/table/tbody/tr[4]/td[2]/span[1]/input[1]').send_keys("1000")
            driver.find_element_by_id("systemVsysSubmit").click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='vsys_name':
                    text_1=input.text
                    if text_1=="vsys_1":
                        match = 1
                        break

            if (not match):
                print ("Add vsys failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VSYS\\001\error_add_vsys.png")
            else:
                success = 1
                print ("Add vsys successfully!!!")

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\001\error_add_vsys1.png")
            print('error:',e)

        finally:
            self.assertTrue(success,msg = 'add vsys failed')
            logout.logout(self)

    def test_002_edit_vsys(self):
        make_path.make_path('./screenshot/VSYS/002')
        driver = self.driver
        success = 0
        try:
            print (u"编辑虚系统")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="systemVsys"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vsys_name':
                    text_1 = input.text
                    if text_1 == "vsys_1":
                        input.click()
                        match_1 = 1
                        break

            if (not match_1):
                print ("cannot find vsys!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VSYS\\002\error_edit_vsys.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="systemVsysForm"]/table/tbody/tr[3]/td[2]/span[1]/input[1]')))
                # 将接口划分到虚系统
                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf1:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupLeft'))).click()
                        break
                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf2:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupLeft'))).click()
                        break
                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf3:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupLeft'))).click()
                        break
                driver.find_element_by_id('systemVsysSubmit').click()
                time.sleep(3)
            # 验证接口是否被划分到虚系统
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'interfaces':
                    text_1 = input.text
                    if text_1 == self.inf1 + ' ' + self.inf2 + ' ' + self.inf3:
                        match_2 = 1
                        break
            if match_2:
                # 将划分到虚系统的接口移回跟系统
                inputs = driver.find_elements_by_tag_name('td')
                for input in inputs:
                    if input.get_attribute('field') == 'vsys_name':
                        text_1 = input.text
                        if text_1 == "vsys_1":
                            input.click()
                            break
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="systemVsysForm"]/table/tbody/tr[3]/td[2]/span[1]/input[1]')))

                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf1:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupRight'))).click()
                        break
                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf2:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupRight'))).click()
                        break
                infs = driver.find_elements_by_tag_name('option')
                for inf in infs:
                    if inf.get_attribute('value') == self.inf3:
                        inf.click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'addrgroupRight'))).click()
                        break
                driver.find_element_by_id('systemVsysSubmit').click()
                time.sleep(3)
            else:
                success = 0
                print('edit vsys failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\002\error_edit_vsys1.png")
            # 验证接口是否被划分到根系统
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_3 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'interfaces':
                    text_1 = input.text
                    if text_1 == self.inf1 + ' ' + self.inf2 + ' ' + self.inf3:
                        match_3 = 1
                        break
            if match_3:
                success = 0
                print('edit vsys failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\002\error_edit_vsys2.png")
            else:
                success = 1

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\002\error_edit_vsys3.png")
            print('error:',e)

        finally:
            self.assertTrue(success,msg = 'edit vsys failed')
            logout.logout(self)

    def test_003_add_vsys_veth(self):
        make_path.make_path('./screenshot/VSYS/003')
        driver = self.driver
        success = 0
        try:
            print (u"添加vsys虚接口")
            login.login(self)
            match_1 = 0
            match_2 = 0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[6]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="vrvethAdd"]/table/tbody/tr[2]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="vrvethAdd"]/table/tbody/tr[2]/td[2]/span/span/a').click()
            time.sleep(2)
            inputs = driver.find_elements_by_tag_name('div')
            for input in inputs:
                if input.get_attribute('class') == "combobox-item":
                    text = input.text
                    if text == "vsys_1":
                        input.click()
                        break
            driver.find_element_by_id('vrvethSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "root_vsys":
                        match_1 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "vsys_1":
                        match_2 = 1
                        break
            if(match_1 and match_2):
                success = 1
            else:
                success = 0
                print('add veth-veth failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\003\error_add_vsys-veth1.png")

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\003\error_add_vsys-veth2.png")
            print('error:',e)

        finally:
            self.assertTrue(success,msg = 'add vsys-veth failed')
            logout.logout(self)

    def test_004_edit_vsys_veth(self):
        make_path.make_path('./screenshot/VSYS/004')
        driver = self.driver
        success = 0
        try:
            print (u"编辑vsys虚接口")
            login.login(self)
            match_1 = 0
            match_2 = 0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[6]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "root_vsys":
                        input.click()
                        match_1 = 1
                        break
            if(match_1):
                wait.until(EC.element_to_be_clickable((By.ID, 'editVrvethBtn'))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="easytabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]')))
                driver.find_element_by_xpath('//*[@id="easytabs"]/div[2]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys('10.10.10.10')
                driver.find_element_by_xpath('//*[@id="easytabs"]/div[2]/div[1]/div/table/tbody/tr/td[4]/span/input[1]').send_keys('255.0.0.0')
                driver.find_element_by_id('add4Cid').click()
                driver.find_element_by_id('vrvethEditSubmit').click()
                time.sleep(3)
            else:
                success = 0
                print('cannot find veth-veth ')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\004\error_edit_vsys-veth.png")
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "ip":
                    text = input.text
                    if text == "IPv4:10.10.10.10/255.0.0.0":
                        match_2 = 1
                        break
            if(match_2):
                success = 1
            else:
                success = 0
                print('edit veth-veth failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\004\error_edit_vsys-veth1.png")
        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\004\error_edit_vsys-veth2.png")
            print('error:',e)

        finally:
            self.assertTrue(success,msg = 'edit vsys-veth failed')
            logout.logout(self)

    def test_005_delete_vsys_veth(self):
        make_path.make_path('./screenshot/VSYS/005')
        driver = self.driver
        success = 0
        try:
            print (u"删除vsys虚接口")
            login.login(self)
            match_1 = 0
            match_2 = 0
            match_3 = 0
            match_4 = 0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[1]/ul/li[6]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "root_vsys":
                        match_1 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "vsys_1":
                        match_2 = 1
                        break
            if(match_1 and match_2):
                driver.find_element_by_xpath('//*[@id="panelBox"]/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td[2]').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteVrvethBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            else:
                success = 0
                print('cannot find veth-veth ')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\005\error_delete_vsys-veth.png")
            wait.until(EC.element_to_be_clickable((By.ID, 'addVrvethBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "root_vsys":
                        match_3 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == "vsys_name":
                    text = input.text
                    if text == "vsys_1":
                        match_4 = 1
                        break

            if(match_3 or match_4):
                success = 0
                print('delete veth-veth failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\005\error_delet_vsys-veth1.png")
            else:
                success = 1

        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\005\error_delete_vsys-veth2.png")
            print('error:',e)

        finally:
            self.assertTrue(success,msg = 'delete vsys-veth failed')
            logout.logout(self)

    def test_006_delete_vsys(self):
        make_path.make_path('./screenshot/VSYS/006')
        driver = self.driver
        success = 0
        try:
            print (u"删除虚系统")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="systemVsys"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_1 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vsys_name':
                    text_1 = input.text
                    if text_1 == "vsys_1":
                        input.click()
                        match_1 = 1
                        break

            if (not match_1):
                print ("cannot find vsys!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\VSYS\\006\error_delete_vsys.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            match_2 = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'vsys_name':
                    text_1 = input.text
                    if text_1 == "vsys_1":
                        match_2 = 1
                        break
            if match_2:
                success = 0
                print('delete vsys failed')
                driver.get_screenshot_as_file(".\screenshot\VSYS\\006\error_delete_vsys1.png")
            else:
                success = 1


        except Exception as e:
            success = 0
            driver.get_screenshot_as_file(".\screenshot\VSYS\\006\error_delete_vsys2.png")
            print('error:',e)

        finally:
            self.assertTrue(success, msg='delete vsys failed')
            logout.logout(self)

    def tearDown(self):
        self.driver.quit()