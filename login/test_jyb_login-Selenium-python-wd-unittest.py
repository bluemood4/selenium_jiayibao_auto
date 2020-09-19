# -*- coding: utf-8 -*-
from selenium import webdriver
from PIL import Image
from baidu_ocr import baid_ocr_to_text#导入百度OCR识别结果
import json
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

user = 'admin'
password = 'jyt987654'


class TestJybLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_jyb_login(self):
        driver = self.driver
        driver.get("http://www.jinyatong.net/index")
        driver.find_element_by_id("userName").send_keys(user)#输入管理系统账号
        driver.find_element_by_id("userpwd").send_keys(password)#输入管理系统密码
        driver.save_screenshot("./code/code.png")#保存当前页面
        code_element = driver.find_element_by_id("vcode")#定位到验证码图片地址
        left = code_element.location['x'] #获取验证码图片的上下左右宽度
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open("./code/code.png")#打开第一次获取的当前页面
        img = im.crop((left,top,right,height))#裁剪出验证码图片
        img.save("./code/vcode.png")#将验证码图片进行保存
        driver.find_element_by_id("validateCode").send_keys(baid_ocr_to_text())#输入识别到的验证码
        driver.find_element_by_css_selector("input.btn-login").click()
        time.sleep(5)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
