#coding=UTF-8
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
from PIL import Image,ImageEnhance
import pytesseract


# 此文件用于自动识别验证码。在2.0版本的webui上试过，正确率可以达到80%以上，但是在2.2上识别的正确率很低。因此在测试时最好找研发去掉验证码。
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
def identify(self):
    try:
        driver=self.driver
        filename_1 = 'C:\Users\Administrator\Desktop\screen\\imge1.png'
        filename_2 = 'C:\Users\Administrator\Desktop\screen\\imge2.png'
        driver.save_screenshot(filename_1)
        imgelemet = driver.find_element_by_id('aimg')
        location = imgelemet.location
        size = imgelemet.size
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
        i = Image.open(filename_1)
        frame4 = i.crop(rangle)
        imgry = frame4.convert('L')
        sharpness = ImageEnhance.Contrast(imgry)
        sharp_img = sharpness.enhance(2.0)
        sharp_img.save(filename_2)
        qq = Image.open(filename_2)
        text = pytesseract.image_to_string(qq)
        time.sleep(2)
        return text
    except Exception as e:
        print(e)
    finally:
        pass

