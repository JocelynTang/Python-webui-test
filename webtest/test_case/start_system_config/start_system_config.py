# coding=UTF-8
from selenium import webdriver
import unittest
import time
from test_case.public import *
import sys
import json
import os
import re
import shutil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append("\ public")


class SYSTEM_CONFIG(unittest.TestCase):
    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/SYSTEM_CONFIG')

    def test_001_config_save_as_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/001')
        driver = self.driver
        success = 0
        try:
            print (u"""另存配置""")
            login.login(self)
            match_1 = 0
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('saveAsBtn').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="configSave"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys('config_1')
            driver.find_element_by_xpath('//*[@id="configSave"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('saved')
            time.sleep(1)
            driver.find_element_by_id('saveAs').click()
            time.sleep(10)

            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'filename':
                    text = input.text
                    if text == 'config_1':
                        match_1 = 1
                        break

            if (match_1 == 1):
                print ('successfully!!!')
                success = 1
            else:
                print ('failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\001\error_config_save_as_file_1.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\001\error_config_save_as_file_1_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_002_export_all_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/002')
        driver = self.driver
        success = 0
        try:
            print (u"""密文整机导出""")
            file_dir = 'C:\Users\\admin\Downloads'
            file_type='.bz2'
            files_1=get_filename.get_filename(file_dir,file_type)
            for file_1 in files_1:
                os.remove(file_1)

            login.login(self)
            time.sleep(3)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('cutBtn').click()
            time.sleep(1)
            driver.find_element_by_id('export1').click()
            time.sleep(1)
            driver.find_element_by_id('exportHtmlSub').click()
            time.sleep(5)

            files_2 = get_filename.get_filename(file_dir, file_type)
            for file_2 in files_2:
                print (file_2)
                if re.match(r'C:\\Users\\admin\\Downloads\\ALL-Config_\d{10}.tar.bz2',file_2):
                    print ('export all config file successfylly')
                    success = 1
                else:
                    print ('failed to export all config file')
                    success = 0
            if success==0:
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\002\error_export_all_config_file.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\002\error_export_all_config_file_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_003_import_all_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/003')
        driver = self.driver
        success = 0
        try:
            print (u"""密文整机导入""")
            file_dir = 'C:\Users\\admin\Downloads'
            file_type = '.bz2'
            filename = []
            files = get_filename.get_filename(file_dir, file_type)
            for file in files:
                if re.match(r'C:\\Users\\admin\\Downloads\\ALL-Config_\d{10}.tar.bz2', file):
                    filename = file
                    break

            login.login(self)
            time.sleep(3)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('importBtn').click()
            time.sleep(1)
            driver.find_element_by_id('import1').click()
            time.sleep(1)
            driver.find_element_by_id('button2').click()
            time.sleep(1)
            driver.find_element_by_id('importFile').send_keys(filename)
            time.sleep(1)
            driver.find_element_by_id('loadf2').click()
            time.sleep(1)
            driver.find_element_by_id('imports').click()
            time.sleep(60)
            success = 1
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\003\import_all_config_file_3.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\003\error_import_all_config_file_3_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_004_export_all_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/004')
        driver = self.driver
        success = 0
        try:
            print (u"""明文整机导出""")
            file_dir = 'C:\Users\\admin\Downloads'
            file_type = '.bz2'
            files_1 = get_filename.get_filename(file_dir, file_type)
            for file_1 in files_1:
                os.remove(file_1)

            login.login(self)
            time.sleep(3)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('cutBtn').click()
            time.sleep(1)
            driver.find_element_by_id('export1').click()
            time.sleep(1)
            driver.find_element_by_id('config_block').click()
            time.sleep(1)
            driver.find_element_by_id('exportHtmlSub').click()
            time.sleep(5)

            files_2 = get_filename.get_filename(file_dir, file_type)
            for file_2 in files_2:
                if re.match(r'C:\\Users\\admin\\Downloads\\ALL-Config_\d{10}.tar.bz2', file_2):
                    print ('export all config file successfylly')
                    success = 1
                else:
                    print ('failed to export all config file')
                    success = 0
            if success == 0:
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\004\error_export_all_config_file.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\004\error_export_all_config_file_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_005_import_all_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/005')
        driver = self.driver
        success = 0
        try:
            print (u"""明文整机导入""")
            file_dir = 'C:\Users\\admin\Downloads'
            file_type = '.bz2'
            filename = []
            files = get_filename.get_filename(file_dir, file_type)
            for file in files:
                if re.match(r'C:\\Users\\admin\\Downloads\\ALL-Config_\d{10}.tar.bz2', file):
                    filename = file

            login.login(self)
            time.sleep(3)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('importBtn').click()
            time.sleep(1)
            driver.find_element_by_id('import1').click()
            time.sleep(1)
            driver.find_element_by_id('button2').click()
            time.sleep(1)
            driver.find_element_by_id('importFile').send_keys(filename)
            time.sleep(1)
            driver.find_element_by_id('loadf2').click()
            time.sleep(1)
            driver.find_element_by_id('imports').click()
            time.sleep(60)
            success = 1
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\005\import_all_config_file_5.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\005\error_import_all_config_file_5_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_006_config_save_as_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/006')
        driver = self.driver
        success = 0
        try:
            print (u"""另存配置""")
            login.login(self)
            time.sleep(3)
            match_1 = 0
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('saveAsBtn').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="configSave"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys('config_2')
            driver.find_element_by_xpath('//*[@id="configSave"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('saved')
            time.sleep(1)
            driver.find_element_by_id('saveAs').click()
            time.sleep(10)

            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'filename':
                    text = input.text
                    if text == 'config_2':
                        match_1 = 1
                        break

            if (match_1 == 1):
                print ('successfully!!!')
                success = 1
            else:
                print ('failed!!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\006\error_config_save_as_file_6.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\006\error_config_save_as_file_6_1.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_007_export_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/007')
        driver = self.driver
        success = 0
        try:
            print (u"""当前密文导出""")
            # 删除导出文件路径下的文件
            file_dir = 'C:\Users\\admin\Downloads'
            for root, dirs, files in os.walk(file_dir):
                for file_1 in files:
                    if re.match(r'config.{0,2}',file_1):
                        os.remove('C:\Users\\admin\Downloads\\'+file_1)

            login.login(self)
            match_1=0
            match_2=0
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            inputs=driver.find_elements_by_tag_name('td')
            # 导出文件
            for input in inputs:
                if input.get_attribute('field')=='filename':
                    text=input.text
                    if text=='config_1':
                        match_1=1
                        input.click()
                        break
            if(match_1==1):
                driver.find_element_by_id('cutBtn').click()
                time.sleep(1)
                driver.find_element_by_id('export').click()
                time.sleep(1)
                driver.find_element_by_id('exportHtmlSub').click()
                time.sleep(5)
            else:
                print ('cannot find config file!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\007\error_export_config_file_7.png")
            #检查文件是否导出成功，若导出成功，则删除设备上的配置文件
            for root, dirs, files in os.walk(file_dir):
                for file_2 in files:
                    if re.match(r'config.{0,2}',file_2):
                        match_2 = 1
                        break
            if(match_2==1):
                print ('export config file successfully')
                success = 1
                driver.find_element_by_id('deleteBtn').click()
                confirm_or_cancel.confirm(self)
                time.sleep(5)
            else:
                success=0
                print ('export config file failed')
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\007\error_export_config_file_7_1.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\007\error_export_config_file_7_2.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_008_import_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/008')
        driver = self.driver
        success = 0
        try:
            print (u"""当前密文导入""")
            filename = []
            file_dir = 'C:\Users\\admin\Downloads'
            for root, dirs, files in os.walk(file_dir):
                for file_1 in files:
                    if re.match(r'config.{0,2}', file_1):
                        filename='C:\Users\\admin\Downloads\\'+file_1
            login.login(self)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('importBtn').click()
            time.sleep(1)
            driver.find_element_by_id('import').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tr1"]/td[2]/span/input[1]').send_keys('1')
            time.sleep(1)
            driver.find_element_by_id('importFile').send_keys(filename)
            time.sleep(1)
            driver.find_element_by_id('imports').click()
            time.sleep(80)
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\008\import_config_file_8.png")
            driver.find_element_by_id('home_menu').click()
            time.sleep(3)
            text=driver.find_element_by_id('systemInfoSystemname').text
            if text=='test':
                success=1
            else:
                success=0
            time.sleep(1)

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\008\error_import_config_file_8.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_009_export_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/009')
        driver = self.driver
        success = 0
        try:
            print (u"""当前明文导出""")
            file_dir = 'C:\Users\\admin\Downloads'
            for root, dirs, files in os.walk(file_dir):
                for file_1 in files:
                    if re.match(r'config.{0,2}',file_1):
                        os.remove('C:\Users\\admin\Downloads\\'+file_1)
            login.login(self)
            match_1=0
            match_2=0
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            inputs=driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field')=='filename':
                    text=input.text
                    if text=='config_2':
                        match_1=1
                        input.click()
                        break
            if(match_1==1):
                driver.find_element_by_id('cutBtn').click()
                time.sleep(1)
                driver.find_element_by_id('export').click()
                time.sleep(1)
                driver.find_element_by_id('config_block').click()
                time.sleep(1)
                driver.find_element_by_id('exportHtmlSub').click()
                time.sleep(5)
            else:
                print ('cannot find config file!!')
                success = 0
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\009\error_export_config_file_9.png")

            for root, dirs, files in os.walk(file_dir):
                for file_2 in files:
                    if re.match(r'config.{0,2}',file_2):
                        match_2 = 1
                        break

            if(match_2==1):
                print ('export config file successfully')
                success = 1
                driver.find_element_by_id('deleteBtn').click()
                confirm_or_cancel.confirm(self)
                time.sleep(5)
            else:
                success=0
                print ('export config file failed')
                driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\009\error_export_config_file_9_1.png")

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\009\error_export_config_file_9_2.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_010_import_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/010')
        driver = self.driver
        success = 0
        try:
            print (u"""当前明文导入""")
            file_dir = 'C:\Users\\admin\Downloads'
            filename = []
            for root, dirs, files in os.walk(file_dir):
                for file_1 in files:
                    if re.match(r'config.{0,2}', file_1):
                        filename='C:\Users\\admin\Downloads\\'+file_1

            login.login(self)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_id('importBtn').click()
            time.sleep(1)
            driver.find_element_by_id('import').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tr1"]/td[2]/span/input[1]').send_keys('1')
            time.sleep(1)
            driver.find_element_by_id('importFile').send_keys(filename)
            time.sleep(1)
            driver.find_element_by_id('imports').click()
            time.sleep(80)
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\010\import_config_file_10.png")
            time.sleep(1)
            driver.find_element_by_id('home_menu').click()
            time.sleep(3)
            text = driver.find_element_by_id('systemInfoSystemname').text
            if text == 'TopsecOS':
                success = 1
            else:
                success = 0

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\010\error_export_config_file_10.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def test_011_delete_config_file(self):
        make_path.make_path('./screenshot/SYSTEM_CONFIG/011')
        driver = self.driver
        success = 0
        try:
            print (u"""删除配置文件""")
            login.login(self)
            driver.find_element_by_id('system_menu').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sysMaintain"]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="config"]/div[1]').click()
            time.sleep(2)
            checkboxes=driver.find_elements_by_tag_name('input')
            for checkbox in checkboxes:
                if checkbox.get_attribute('name')=='ck':
                    checkbox.click()
            driver.find_element_by_id('deleteBtn').click()
            time.sleep(2)
            confirm_or_cancel.confirm(self)
            time.sleep(5)
            success = 1

        except Exception as e:
            print('error:', e)
            success = 0
            driver.get_screenshot_as_file(".\screenshot\SYSTEM_CONFIG\\011\error_delete_file.png")

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
