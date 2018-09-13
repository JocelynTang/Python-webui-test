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


class DHCP(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser_type.set_browser()
        make_path.make_path('./screenshot/DHCP')

    def test_001_add_dhcp_pool(self):
        make_path.make_path('./screenshot/DHCP/001')
        driver = self.driver
        success = 0
        try:
            print (u"""添加地址池""")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID,'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dhcp"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.ID, 'dhcpPoolAdd'))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="dhcpPoolAddForm"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/span[1]/input[1]'))).send_keys('30.1.1.0')
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="dhcpPoolAddForm"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/span[2]/input[1]'))).send_keys('255.255.255.0')
            driver.find_element_by_xpath('//*[@id="dhcpPoolAddForm"]/div[2]/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('30.1.1.2')
            driver.find_element_by_xpath('//*[@id="dhcpPoolAddForm"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/span/input[1]').send_keys('30.1.1.110')
            driver.find_element_by_id('dhcpPoolAddSubmit').click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'dhcpPoolAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'area':
                    text = input.text
                    if text == '30.1.1.0/255.255.255.0':
                        match = 1
                        break

            if (not match):
                print ('Add dhcp pool failed !')
                driver.get_screenshot_as_file(".\screenshot\DHCP\\001\error_add_dhcp_pool.png")
                success=0
            else:
                print ('Add dhcp pool successfully !')
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\001\error_add_dhcp_pool_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'add dhcp pool failed')

    def test_002_start_dhcp_server(self):
        make_path.make_path('./screenshot/DHCP/002')
        driver = self.driver
        success = 0
        try:
            print (u"""开启DHCP服务端""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="leftSelectItemCid"]/option[2]'))).click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('serverBtnStart').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'serverBtnStop')))
            text_1=driver.find_element_by_id('serverBtnStart').get_attribute('disabled')
            print (text_1)
            text_2=driver.find_element_by_id('serverBtnStop').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if (text_1 and not text_2):
                print ("Start dhcp server successfully !")
                success = 1
            else:
                print ("Start dhcp server failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\002\error_start_dhcp_server.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\002\error_start_dhcp_server_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'start dhcp server failed')

    def test_003_stop_dhcp_client(self):
        make_path.make_path('./screenshot/DHCP/003')
        driver = self.driver
        success = 0
        try:
            print (u"""关闭DHCP服务端""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            time.sleep(1)
            driver.find_element_by_id('serverBtnStop').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'serverBtnStart')))
            text_1=driver.find_element_by_id('serverBtnStart').get_attribute('disabled')
            print (text_1)
            text_2=driver.find_element_by_id('serverBtnStop').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if (not text_1 and text_2):
                print ("Stop dhcp server successfully !")
                success = 1
            else:
                print ("Stop dhcp server failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\003\error_stop_dhcp_server.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\003\error_stop_dhcp_server_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg ='stop dhcp server failed')

    def test_004_clear_dhcp_pool(self):
        make_path.make_path('./screenshot/DHCP/004')
        driver = self.driver
        success = 0
        try:
            print (u"""清空地址池""")
            match = 0
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            time.sleep(1)
            driver.find_element_by_id('dhcpPoolClear').click()
            time.sleep(1)
            confirm_or_cancel.confirm(self)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID,'dhcpPoolAdd')))
            inputs = driver.find_elements_by_tag_name('td')
            for input in inputs:
                if input.get_attribute('field') == 'area':
                    text = input.text
                    if text == '30.1.1.0/255.255.255.255.0':
                        match = 1
                        break

            if (match):
                print ('Clear dhcp pool failed !')
                driver.get_screenshot_as_file(".\screenshot\DHCP\\004\error_clear_dhcp_pool.png")
                success=0
            else:
                print ('Clear dhcp pool successfully !')
                success = 1

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\004\error_clear_dhcp_pool_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'clear dhcp pool failed')

    def test_005_start_dhcp_client(self):
        make_path.make_path('./screenshot/DHCP/005')
        driver = self.driver
        success = 0
        try:
            print (u"""开启DHCP客户端""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fd-tabs"]/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[2]'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftSelectItemCid"]/option[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftSelectItemCid"]/option[2]'))).click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_id('clientBtnStart').click()
            time.sleep(10)
            wait.until(EC.element_to_be_clickable((By.ID, 'clientBtnStop')))
            text_1=driver.find_element_by_id('clientBtnStart').get_attribute('disabled')
            print (text_1)
            text_2=driver.find_element_by_id('clientBtnStop').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if (text_1 and not text_2):
                print ("Start dhcp client successfully !")
                success = 1
            else:
                print ("Start dhcp client failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\005\error_start_dhcp_client.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\005\error_start_dhcp_client_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'start dhcp client failed')

    def test_006_stop_dhcp_client(self):
        make_path.make_path('./screenshot/DHCP/006')
        driver = self.driver
        success = 0
        try:
            print (u"""关闭DHCP客户端""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fd-tabs"]/li[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[2]'))).click()
            time.sleep(1)
            driver.find_element_by_id('clientBtnStop').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'clientBtnStart')))
            text_1=driver.find_element_by_id('clientBtnStart').get_attribute('disabled')
            print (text_1)
            text_2=driver.find_element_by_id('clientBtnStop').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if (not text_1 and text_2):
                print ("Stop dhcp client successfully !")
                success = 1
            else:
                print ("Stop dhcp client failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\006\error_stop_dhcp_client.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\006\error_stop_dhcp_client_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success,msg = 'stop dhcp client failed')

    def test_007_start_dhcp_relay(self):
        make_path.make_path('./screenshot/DHCP/007')
        driver = self.driver
        success = 0
        try:
            print (u"""开启DHCP中继""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fd-tabs"]/li[3]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[3]'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftSelectItemCid"]/option[2]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leftSelectItemCid"]/option[2]'))).click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_xpath('//*[@id="leftSelectItemCid"]/option[2]').click()
            driver.find_element_by_id('addrgroupLeft').click()
            driver.find_element_by_xpath('//*[@id="dhcpBox"]/div[1]/fieldset/span/span[2]/input[1]').send_keys('30.1.1.120')
            driver.find_element_by_id('relayBtnStart').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'relayBtnStop')))

            text_1 = driver.find_element_by_id('relayBtnStart').get_attribute('disabled')
            print (text_1)
            text_2 = driver.find_element_by_id('relayBtnStop').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if(text_1 and not text_2):
                print ("Start dhcp relay successfully !")
                success = 1
            else:
                print ("Start dhcp relay failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\007\error_start_dhcp_relay.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\007\error_start_dhcp_relay_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='start dhcp relay failed')

    def test_008_stop_dhcp_relay(self):
        make_path.make_path('./screenshot/DHCP/008')
        driver = self.driver
        success = 0
        try:
            print (u"""关闭DHCP中继""")
            login.login(self)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'network_menu'))).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dhcp"]/div[1]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dhcp"]/div[1]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fd-tabs"]/li[3]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fd-tabs"]/li[3]'))).click()
            time.sleep(1)
            driver.find_element_by_id('relayBtnStop').click()
            wait.until(EC.element_to_be_clickable((By.ID, 'relayBtnStart')))

            text_1 = driver.find_element_by_id('relayBtnStop').get_attribute('disabled')
            print (text_1)
            text_2 = driver.find_element_by_id('relayBtnStart').get_attribute('disabled')
            print (text_2)
            time.sleep(1)
            if (text_1 and not text_2):
                print ("Stop dhcp relay successfully !")
                success = 1
            else:
                print ("Stop dhcp relay failed !")
                success = 0
                driver.get_screenshot_as_file('.\screenshot\DHCP\\008\error_stop_dhcp_relay.png')

        except Exception as e:
            driver.get_screenshot_as_file(".\screenshot\DHCP\\008\error_stop_dhcp_relay_1.png")
            print ('error:',e)
            success = 0

        finally:
            logout.logout(self)
            self.assertTrue(success, msg='stop dhcp relay failed')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
