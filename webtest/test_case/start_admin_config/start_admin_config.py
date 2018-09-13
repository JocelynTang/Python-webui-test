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


class ADMIN_CONFIG(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        # 创建目录用于存放截图
        make_path.make_path('./screenshot/ADMIN_CONFIG')

    def test_001_admin_set(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/001')
        success = 0
        driver = self.driver
        try:
            print (u'管理员设置')
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'typeSet'))).click()
            # 密码复杂度低
            wait.until(EC.element_to_be_clickable((By.ID, 'passwordLow'))).click()
            # 管理员最大在线数 5000
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="parameterForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="parameterForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="parameterForm"]/table/tbody/tr[5]/td[2]/span[1]/input[1]').send_keys(
                '5000')
            # 同一个管理员最大在线数 5000
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="parameterForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]')))
            driver.find_element_by_xpath('//*[@id="parameterForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="parameterForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]').send_keys(
                '5000')
            driver.find_element_by_id('adminSet').click()
            time.sleep(5)
            x = driver.find_element_by_xpath(
                '//*[@id="parameterForm"]/table/tbody/tr[5]/td[2]/span[1]/input[2]').get_attribute('value')
            y = driver.find_element_by_xpath(
                '//*[@id="parameterForm"]/table/tbody/tr[6]/td[2]/span[1]/input[2]').get_attribute('value')
            if x == y == '5000':
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\001\error_admin_set_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='set admin parameters failed')

    def test_002_add_manage_permission(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/002')
        driver=self.driver
        success = 0
        try:
            print (u"""添加管理员权限模板""")
            match = 0
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'typePer'))).click()
            # 添加管理权限模板 拥有读所有模块的权限
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtnPower'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="limitAddForm"]/table/tbody/tr[1]/td[2]/span/input[1]')))
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="limitAddForm"]/table/tbody/tr[1]/td[2]/span/input[1]'))).send_keys('admin_1')
            wait.until(EC.element_to_be_clickable((By.ID, 'ckRead'))).click()
            driver.find_element_by_id('addlimit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtnPower')))
            admins=driver.find_elements_by_tag_name('td')
            for admin in admins:
                if admin.get_attribute('field')=='map_name':
                    text=admin.text
                    if text=='admin_1':
                        match = 1
                        break
            if(not match):
                print ('add manage permission failed!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\002\error_add_manage_permission.png")
                success=0
            else:
                print ('add manage permission successfully!!!')
                success=1
        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\002\error_add_manage_permission_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add manage permission failed')

    def test_003_add_admin(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/003')
        driver = self.driver
        success = 0
        try:
            print (u"""添加管理员""")
            login.login(self)

            match = 0
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="adminAddForm"]/table/tbody/tr[1]/td[2]/span/input[1]'))).send_keys('test_1')
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="adminAddForm"]/table/tbody/tr[6]/td[2]/span[1]/input[1]'))).send_keys('talent123')
            driver.find_element_by_xpath('//*[@id="adminAddForm"]/table/tbody/tr[7]/td[2]/span/input[1]').send_keys(
                'talent123')
            driver.find_element_by_xpath('//*[@id="adminAddForm"]/table[1]/tbody/tr[9]/td[2]/span/input[1]').click()
            time.sleep(1)
            types = driver.find_elements_by_tag_name('div')
            for type in types:
                if type.get_attribute('class') == 'combobox-item':
                    text = type.text
                    if text == 'admin_1':
                        type.click()
                        break
            driver.find_element_by_id('none').click()
            driver.find_element_by_id('addAdmin').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='admin_name':
                    text=input.text
                    if text=='test_1':
                        match=1
                        break
            if(not match):
                print ('add admin failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\003\error_add_admin.png")
            else:
                print ('add admin successfully!!!')
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\003\error_add_admin_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add admin failed')

    def test_004_edit_manage_permission(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/004')
        driver = self.driver
        success = 0
        try:
            print (u"""编辑管理员权限模板""")
            match_1 = 0
            match_2 = 0
            login.login(self)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'typePer'))).click()
            time.sleep(1)
            admins = driver.find_elements_by_tag_name('td')
            for admin in admins:
                if admin.get_attribute('field') == 'map_name':
                    text = admin.text
                    if text == 'admin_1':
                        match_1 = 1
                        admin.click()
                        break
            if (not match_1):
                print ('cannot find object!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\004\error_edit_manage_permission.png")
                success = 0
            else:
                # 将权限模板的权限修改为读写
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtnPower'))).click()
                time.sleep(1)
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="limitAddForm"]/table/tbody/tr[2]/td[2]/span/input[1]')))
                driver.find_element_by_xpath('//*[@id="limitAddForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(
                    'editedbytql')
                driver.find_element_by_id('ckWrite').click()
                driver.find_element_by_id('addlimit').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'editBtnPower')))
            ads=driver.find_elements_by_tag_name('td')
            for ad in ads:
                if ad.get_attribute('field')=='map_name':
                    text=ad.text
                    if text=='admin_1':
                        match_2 = 1
                        break

            if(not match_2):
                print ('edit manage permission failed!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\004\error_edit_manage_permission.png")
                success=0
            else:
                print ('edit manage permission successfully!!!')
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\004\error_edit_manage_permission_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit manage permission failed')

    def test_005_edit_admin(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/005')
        driver = self.driver
        success = 0
        try:
            print (u"""编辑管理员""")
            match_1=0
            match_2=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            time.sleep(1)
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'admin_name':
                    text = input.text
                    if text == 'test_1':
                        match_1 = 1
                        input.click()
                        break
            if (not match_1):
                print ('cann\'t find admin!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\005\error_edit_admin.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID, 'editBtn'))).click()
                time.sleep(1)
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="adminAddForm"]/table[1]/tbody/tr[2]/td[2]/span/input[1]'))).clear()
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="adminAddForm"]/table[1]/tbody/tr[2]/td[2]/span/input[1]'))).send_keys('edited')
                driver.find_element_by_id('changePwd').click()
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="adminAddForm"]/table[1]/tbody/tr[6]/td[2]/span/input[1]')))
                driver.find_element_by_xpath(
                    '//*[@id="adminAddForm"]/table[1]/tbody/tr[6]/td[2]/span/input[1]').send_keys('topsec123456')
                driver.find_element_by_xpath(
                    '//*[@id="adminAddForm"]/table[1]/tbody/tr[7]/td[2]/span/input[1]').send_keys('topsec123456')
                driver.find_element_by_id('addAdmin').click()
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn')))
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') == 'admin_name':
                    text = output.text
                    if text == 'test_1':
                        match_2 = 1
                        break
            if(not match_2):
                print ('edit admin failed!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\005\error_edit_admin_1.png")
            else:
                print ('edit admin successfully!!!')
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\005\error_edit_admin_2.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'edit admin failed')

    def test_006_delete_admin(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/006')
        driver = self.driver
        success = 0
        try:
            print (u"""删除管理员""")
            match_1=0
            match_2=0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            time.sleep(1)
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='admin_name':
                    text=input.text
                    if text=='test_1':
                        match_1=1
                        input.click()
                        break
            if(not match_1):
                print ('cann\'t find admin!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\006\error_delete_admin.png")
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'deleteBtn'))).click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtn'))).click()
            outputs = driver.find_elements_by_tag_name('td')
            for output in outputs:
                if output.get_attribute('field') == 'admin_name':
                    text = output.text
                    if text == 'test_1':
                        match_2 = 1
                        break
            if(match_1 and not match_2):
                print ('delete admin successfully!!!')
                success = 1

            else:
                print ('delete admin failed!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\006\error_delete_admin_1.png")

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\006\error_delete_admin_2.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'delete admin failed')

    def test_007_delete_manage_permission(self):
        make_path.make_path('./screenshot/ADMIN_CONFIG/007')
        driver = self.driver
        success = 0
        try:
            print (u"""删除管理员权限模板""")
            match_1 = 0
            match_2 = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'system_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Administrator"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Administrator"]/div[1]'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'typePer'))).click()
            time.sleep(1)
            admins = driver.find_elements_by_tag_name('td')
            for admin in admins:
                if admin.get_attribute('field') == 'map_name':
                    text = admin.text
                    if text == 'admin_1':
                        match_1 = 1
                        admin.click()
                        break
            if (not match_1):
                print ('cannot find object!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\007\error_delete_manage_permission.png")
                success = 0
            else:
                wait.until(EC.element_to_be_clickable((By.ID,'deleteBtnPower')))
                driver.find_element_by_id('deleteBtnPower').click()
                time.sleep(1)
                confirm_or_cancel.confirm(self)
                time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'addBtnPower')))
            ads = driver.find_elements_by_tag_name('td')
            for ad in ads:
                if ad.get_attribute('field') == 'map_name':
                    text = ad.text
                    if text == 'admin_1':
                        match_2 = 1
                        break

            if (match_1 and not match_2):
                print ('delete manage permission successfully!!!')
                success = 1

            else:
                print ('delete manage permission failed!!!')
                driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\007\error_delete_manage_permission.png")
                success = 0

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\ADMIN_CONFIG\\007\error_delete_manage_permission_1.png")
            print ('error:', e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='delete manage permission failed')

    def tearDown(self):
        self.driver.quit()

def suite():
    return unittest.makeSuite(ADMIN_CONFIG,'test')

if __name__=="__main__":
    unittest.main()
