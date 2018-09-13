# coding = utf-8
from selenium import webdriver
import time


driver = webdriver.Safari()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.close()
