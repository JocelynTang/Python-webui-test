#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time,re
import sys

# 此文件可用于确认页面上是否存在某个元素，存在返回True，不存在返回False
# 当前只写了find id，可以根据需要扩展name、class name等等
def is_element_exist(self,element):
    try:
        driver=self.driver
        f=True
        driver.find_element_by_id(element)
        return f

    except:
        f=False
        return f
    finally:
        pass
