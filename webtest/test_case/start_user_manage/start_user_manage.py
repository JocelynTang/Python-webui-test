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


class USER_MANAGE(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/USER_MANAGE')

    def test_001_add_localauthserver(self):
        make_path.make_path('./screenshot/USER_MANAGE/001')
        driver = self.driver
        success = 0
        try:
            print (u"添加本地认证服务器")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]').send_keys('localserver1')
            driver.find_element_by_id('addServer').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='server_name':
                    text = input.text
                    if text=='localserver1':
                        match = 1
                        break
            if match:
                print ('add local auth server successfully')
                success = 1
            else:
                print ('add local auth server failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\001\error_add_localserver.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\001\error_add_localserver_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add local auth server failed')

    def test_002_add_radiusauthserver(self):
        make_path.make_path('./screenshot/USER_MANAGE/002')
        driver = self.driver
        success = 0
        try:
            print (u"添加radius认证服务器")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_id('labelRadio2').click()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]').send_keys('radiusserver1')
            driver.find_element_by_xpath('//*[@id="localAddr"]/td[2]/span/input[1]').send_keys('172.18.20.146')
            driver.find_element_by_xpath('//*[@id="radius2"]/td[2]/span/input[1]').send_keys('talent')
            driver.find_element_by_id('addServer').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='server_name':
                    text = input.text
                    if text=='radiusserver1':
                        match = 1
                        break
            if match:
                print ('add radius server successfully')
                success = 1
            else:
                print ('add radius server failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\002\error_add_radiusserver.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\002\error_add_radiusserver_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add radius server failed')

    def test_003_add_ldapauthserver(self):
        make_path.make_path('./screenshot/USER_MANAGE/003')
        driver = self.driver
        success = 0
        try:
            print (u"添加ldap认证服务器")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_id('labelRadio3').click()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]').send_keys('ldapserver1')
            driver.find_element_by_xpath('//*[@id="localAddr"]/td[2]/span/input[1]').send_keys('172.18.20.145')
            driver.find_element_by_xpath('//*[@id="ldap1"]/td[2]/span/input[1]').send_keys('dc=test,dc=com')
            driver.find_element_by_id('addServer').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='server_name':
                    text = input.text
                    if text=='ldapserver1':
                        match = 1
                        break
            if match:
                print ('add ldap server successfully')
                success = 1
            else:
                print ('add ldap server failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\003\error_add_ldapserver.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\003\error_add_ldapserver_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add ldap server failed')

    def test_004_add_tacacsauthserver(self):
        make_path.make_path('./screenshot/USER_MANAGE/004')
        driver = self.driver
        success = 0
        try:
            print (u"添加tacacs认证服务器")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID,'addBtn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_id('labelRadio4').click()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[4]/td[2]/span/input[1]').send_keys('tacacsserver1')
            driver.find_element_by_xpath('//*[@id="localAddr"]/td[2]/span/input[1]').send_keys('172.18.20.146')
            driver.find_element_by_xpath('//*[@id="radius2"]/td[2]/span/input[1]').send_keys('talent')
            driver.find_element_by_id('addServer').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='server_name':
                    text = input.text
                    if text=='tacacsserver1':
                        match = 1
                        break
            if match:
                print ('add tacacs server successfully')
                success = 1
            else:
                print ('add tacacs server failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\004\error_add_tacacsserver.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\004\error_add_tacacsserver_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add tacacs server failed')

    def test_005_add_localuser(self):
        make_path.make_path('./screenshot/USER_MANAGE/005')
        driver = self.driver
        success = 0
        try:
            print (u"添加本地用户")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('localuser1')
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[6]/td[2]/span/span').click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == u"本地认证":
                        type.click()
                        break
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="localServerSpan"]/td[2]/span/span/span').click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == "localserver1":
                        type.click()
                        break
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="localPwdConf"]/td[2]/span/input[1]').send_keys('talent')
            driver.find_element_by_xpath('//*[@id="localMailConf"]/td[2]/span/input[1]').send_keys('123@qq.com')
            driver.find_element_by_xpath('//*[@id="localPhoneConf"]/td[2]/span/input[1]').send_keys('13812345678')
            driver.find_element_by_id('addUserInfo').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localuser1':
                        match = 1
                        break
            if match:
                print ('add local user successfully')
                success = 1
            else:
                print ('add local user failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\005\error_add_localuser.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\005\error_add_localuser_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add local user failed')


    def test_006_add_externaluser(self):
        make_path.make_path('./screenshot/USER_MANAGE/006')
        driver = self.driver
        success = 0
        try:
            print (u"添加外部认证用户")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[2]/td[2]/span[1]/input[1]').send_keys('externaluser1')
            driver.find_element_by_xpath('//*[@id="setstyles"]/tbody/tr[6]/td[2]/span/span').click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == u"外部认证":
                        type.click()
                        break
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="remoteServerSpan"]/td[2]/span/span/span/a').click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == "radiusserver1":
                        type.click()
                        break
            time.sleep(1)
            driver.find_element_by_id('addUserInfo').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'externaluser1':
                        match = 1
                        break
            if match:
                print ('add external user successfully')
                success = 1
            else:
                print ('add external user failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\006\error_add_externaluser.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\006\error_add_externaluser_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add external user failed')

    def test_007_add_portal(self):
        make_path.make_path('./screenshot/USER_MANAGE/007')
        driver = self.driver
        success = 0
        try:
            print (u"添加认证门户")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftMenuBox"]/ul/li[3]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[3]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addIcn'))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="portalForm"]/table/tbody/tr[1]/td[2]/span/input[1]')))
            driver.find_element_by_xpath('//*[@id="portalForm"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys('localportal1')
            # 目前只测试门户是否可以添加，不测试是否可以认证，后续如果需要测试是否可以认证，可以通过读取配置文件来获取ip地址
            driver.find_element_by_xpath('//*[@id="portalForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('1.1.1.1')
            driver.find_element_by_xpath('//*[@id="portalForm"]/table/tbody/tr[3]/td[2]/span/input[1]').send_keys('8085')
            driver.find_element_by_xpath('//*[@id="portalForm"]/table/tbody/tr[4]/td[2]/span/span').click()
            time.sleep(2)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == "localserver1":
                        type.click()
                        break
            time.sleep(1)
            driver.find_element_by_id('portalSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addIcn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localportal1':
                        match = 1
                        break
            if match:
                print ('add local portal successfully')
                success = 1
            else:
                print ('add local portal failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\007\error_add_localportal.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\007\error_add_localportal_1.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='add local portal failed')

    def test_008_delete_portal(self):
        make_path.make_path('./screenshot/USER_MANAGE/008')
        driver = self.driver
        success = 0
        try:
            print (u"删除认证门户")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftMenuBox"]/ul/li[3]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[3]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addIcn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localportal1':
                        match_1 = 1
                        input.click()
                        time.sleep(1)
                        break
            if match_1:
                wait.until(EC.element_to_be_clickable((By.ID, 'deleteIcn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            else:
                print ('cannot find local portal ')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\008\error_delete_localportal.png')

            wait.until(EC.element_to_be_clickable((By.ID, 'addIcn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localportal1':
                        match_2 = 1
                        break
            if match_2:
                print ('delete local portal failed')
                success = 0
                driver.get_screenshot_as_file('.\screenshot\USER_MANAGE\\008\error_delete_localportal_1.png')
            else:
                success = 1
                print('delete local portal successfully')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\008\error_delete_localportal_2.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete local portal failed')

    def test_009_delete_users(self):
        make_path.make_path('./screenshot/USER_MANAGE/009')
        driver = self.driver
        success = 0
        try:
            print (u"删除用户")
            match_1 = 0
            match_2 = 0
            match_3 = 0
            match_4 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'externaluser1':
                        match_1 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localuser1':
                        match_2 = 1
                        break
            if not match_2 or not match_1:
                success = 0
                print('cannot find all users')
                driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\009\error_delete_users.png")
            else:
                driver.find_element_by_xpath('//*[@id="userBox"]/div[4]/div/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td[2]').click()
                wait.until(EC.element_to_be_clickable((By.ID,'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)

            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'externaluser1':
                        match_3 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localuser1':
                        match_4 = 1
                        break
            if match_3 or match_4:
                success = 0
                print('delete users failed')
                driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\009\error_delete_users_1.png")
            else:
                success = 1
                print("delete all users successfully")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\009\error_delete_users_2.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete users failed')

    def test_010_delete_servers(self):
        make_path.make_path('./screenshot/USER_MANAGE/010')
        driver = self.driver
        success = 0
        try:
            print (u"删除认证服务器")
            match_1 = 0
            match_2 = 0
            match_3 = 0
            match_4 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'authManage_menu'))).click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftMenuBox"]/ul/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            driver.find_element_by_xpath('//*[@id="panelBox"]/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td[2]/div/input').click()
            wait.until(EC.element_to_be_clickable((By.ID,'deleteBtn'))).click()
            confirm_or_cancel.confirm(self)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'localserver1':
                        match_1 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'radiusserver1':
                        match_2 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'ldapserver1':
                        match_3 = 1
                        break
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'name':
                    text = input.text
                    if text == 'tacacsserver1':
                        match_4 = 1
                        break

            if match_1 or match_2 or match_3 or match_4:
                success = 0
                print("delete servers failed")
                driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\010\error_delete_servers_1.png")
            else:
                success = 1
                print('delete servers successfully')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\USER_MANAGE\\009\error_delete_servers_2.png")
            print ('error:', e)
            success = 0
        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete users failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()