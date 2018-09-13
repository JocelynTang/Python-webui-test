# coding=UTF-8
import time


# 此函数用于处理删除、清空以及部分应用操作界面弹出的确认提示框，弹出提示时点击“确认”按钮
def confirm(self):
    try:
        driver = self.driver
        buttons = driver.find_elements_by_tag_name('span')
        for button in buttons:
            if button.get_attribute('class') == 'l-btn-text':
                text_2 = button.text
                if text_2 == u"确定":
                    button.click()
                    time.sleep(2)
                    break
    except Exception as e:
        print('error:', e)


# 此函数用于处理删除、清空以及部分应用操作界面弹出的确认提示框，弹出提示时点击“取消”按钮
def cancel(self):
    try:
        driver = self.driver
        buttons = driver.find_elements_by_tag_name('span')
        for button in buttons:
            if button.get_attribute('class') == 'l-btn-text':
                text_2 = button.text
                if text_2 == u"取消":
                    button.click()
                    time.sleep(2)
                    break
    except Exception as e:
        print('error:', e)
