# coding=utf-8
import unittest
import HTMLTestRunner
import time
import os
import allcase_list
import shutil
import send_email
import do_system_config_reset


def run_webui_test():
    # 创建screenshot目录，以存放截图
    if os.path.exists('./screenshot'):
        shutil.rmtree('./screenshot')
        os.mkdir('./screenshot')
    else:
        os.mkdir('./screenshot')

    # 读取要执行的用例，生成测试用例集
    alltestnames = allcase_list.caselist()
    testunit = unittest.TestSuite()
    for test in alltestnames:
        testunit.addTest(unittest.makeSuite(test))

    # 生成测试报告，测试报告以开始执行用例的时间命名
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = '.\\report\\' + now + 'result.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        # verbosity=2,
        title=u'NGTOS WEBUI测试报告',
        description=u'用例执行情况：')
    # 执行用例
    runner.run(testunit)


if __name__ == '__main__':
    # while True:
    #     # 重置设备配置
    #     do_system_config_reset.config_reset()
    #     # 执行测试脚本
    #     run_webui_test()
    #     # 发送邮件
    #     send_email.send_email()
    #     # 为了避免一些问题，sleep 300s后再执行下一次
    #     time.sleep(300)
    # # 重置设备配置
    # do_system_config_reset.config_reset()
    # # 执行测试脚本
    run_webui_test()
    # 发送邮件
    # send_email.send_email()
