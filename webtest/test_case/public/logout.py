#coding=UTF-8
import time


# 此文件用于退出webui
def logout(self):
    try:
        driver = self.driver
        print('>>>logout now!wait....')
        driver.find_element_by_id("prepareLogout").click()
        time.sleep(1)
        # driver.find_element_by_id("saveChecked").click()
        # time.sleep(1)
        driver.find_element_by_id('logoutSubmit').click()
        time.sleep(5)
        driver.get_screenshot_as_file("./screenshot/log_out.png")
    except Exception as e:
        print('error:',e)
