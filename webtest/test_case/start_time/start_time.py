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


class TIME(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/TIME')

    def test_001_add_cycle_time(self):
        make_path.make_path('./screenshot/TIME/001')
        driver = self.driver
        success = 0
        try:
            print (u"""添加循环时间对象""")
            login.login(self)
            wait=WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'circleTypeDay')))
            driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("cycletime_1")
            driver.find_element_by_id('circleTypeDay').click()
            driver.find_element_by_id('addCirTime').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="cycletime_1":
                        match = 1
                        break
            if (not match):
                print ("Add cycle time failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\001\error_add_cycle_time.png")
            else:
                print ("Add cycle time successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\001\error_add_cycle_time1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add cycle time failed')

    def test_002_edit_cycle_time(self):
        make_path.make_path('./screenshot/TIME/002')
        driver = self.driver
        success = 0
        try:
            print (u"""修改循环时间对象""")
            login.login(self)

            match_1=0
            match_2=0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="cycletime_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No cycle time founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\002\error_edit_cycle_time.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'cycleEdit'))).click()
                time.sleep(1)
                driver.find_element_by_id('cycleShareOn').click()
                driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/span[2]/input[1]').clear()
                driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/span[2]/input[1]').send_keys('10:00')
                driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/span[3]/input[1]').clear()
                driver.find_element_by_xpath('//*[@id="cycleAddForm"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/span[3]/input[1]').send_keys('20:00')
                driver.find_element_by_id('addCirTime').click()
                time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="cycletime_1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit cycle time failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\002\error_edit_cycle_time.png")
            else:
                print ("Edit cycle time successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\002\error_edit_cycle_time1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit cycle time failed')

    def test_006_delete_cycle_time(self):
        make_path.make_path('./screenshot/TIME/006')
        driver = self.driver
        success = 0
        try:
            print (u"""删除循环时间对象""")
            login.login(self)
            match_1=0
            match_2=0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="cycletime_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No cycle time founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\006\error_delete_cycle_time.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'cycleDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'cycleAdd')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="cycletime_1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete cycle time successfully!!!")
                success = 1
            else:
                print ("Delete cycle time failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\006\error_delete_cycle_time.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\006\error_delete_cycle_time1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete cycle time failed')

    def test_003_add_time_group(self):
        make_path.make_path('./screenshot/TIME/003')
        driver = self.driver
        success = 0
        try:
            print (u"""添加时间组对象""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang') == 'TIME_GROUP':
                    name.click()
                    break
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[1]/td[2]/span[1]/input[1]').send_keys("timegroup_1")
            driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option').click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('addTimeGro').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd')))
            match = 0
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="timegroup_1":
                        match = 1
                        input.click()
                        break
            if (not match):
                print ("Add time group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\003\error_add_time_group.png")
            else:
                print ("Add time group successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\003\error_add_time_group1.png")
            print('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add time group failed')

    def test_004_edit_time_group(self):
        make_path.make_path('./screenshot/TIME/004')
        driver = self.driver
        success = 0
        try:
            print (u"""修改时间组对象""")
            login.login(self)
            match_1=0
            match_2=0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang') == 'TIME_GROUP':
                    name.click()
                    break
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="timegroup_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No time group founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\004\error_add_time_group.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'groupEdit'))).click()
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, 'shareOn'))).click()
                driver.find_element_by_id('addTimeGro').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="timegroup_1":
                        match_2 = 1
                        break
            if (not match_2):
                print ("Edit time group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\004\error_edit_time_group.png")
            else:
                print ("Edit time group successfully!!!")
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\004\error_edit_time_group1.png")
            print('error:',e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit time group failed')

    def test_005_time_group_delete(self):
        make_path.make_path('./screenshot/TIME/005')
        driver = self.driver
        success = 0
        try:
            print (u"""删除时间组对象""")
            login.login(self)

            match_1=0
            match_2=0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'policy_menu'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="object"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedule"]/div[1]'))).click()
            time.sleep(1)
            names = driver.find_elements_by_tag_name('a')
            for name in names:
                if name.get_attribute('lang') == 'TIME_GROUP':
                    name.click()
                    break
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') =='name':
                    text=input.text
                    if text=="timegroup_1":
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ("No time group founded!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\005\error_add_time_group.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'groupDelete'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'groupAdd')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') =='name':
                    text=output.text
                    if text=="timegroup_1":
                        match_2 = 1
                        break
            if (match_1 and not match_2):
                print ("Delete time group successfully!!!")
                success = 1
            else:
                print ("Delete time group failed!!!")
                success = 0
                driver.get_screenshot_as_file(".\screenshot\TIME\\005\error_delete_time_group.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\TIME\\005\error_delete_time_group1.png")
            print('error:',e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete time group failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

