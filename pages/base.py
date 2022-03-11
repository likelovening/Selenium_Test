#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/10/20
_data_='二次封装selenium基类、获取EOMS验证码'
"""
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import  webdriver
import os
from PIL import Image
from PIL import ImageEnhance
from pytesseract import pytesseract
from selenium.common import exceptions

class Base_pages(object):
    #初始化driver、url
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    #查找元素
    def Find_element(self,elem):
        #return self.driver.find_element(*elem)
        try:
            #设置等待元素出现
            return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(elem))
        except :
            print("获取元素失败")
    #校验专用元素查询
    def Find_elements(self, elem):
        return self.driver.find_element_by_xpath(elem)

    #输入框进行输入
    def input_send_keys(self,elem,text):
        try:
            self.Find_element(elem).clear()
            self.Find_element(elem).send_keys(text)
        except:
            self.Find_element(elem).send_keys(text)

    #清理输入框内容
    def clear_input(self,elem):
        self.Find_element(elem).clear()

    #元素点击
    def click(self,elem):
        self.Find_element(elem).click()

    #js元素点击
    def js_click(self,elem):
        self.driver.execute_script("arguments[0].click();",self.Find_elements(elem))

    #获取界面文本
    def get_text(self,elem):
        return self.Find_element(elem).text

    #切换frame
    def switch_frame(self,frame):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(frame))

    #切换回默认窗口
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    #切换handles界面
    def changes_handles(self,num):
        new_windows=self.driver.window_handles
        self.driver.switch_to.window(new_windows[num])

    #弹框确认
    def alert_confirm(self):
        alert_enter=self.driver.switch_to.alert
        alert_enter.accept()

    #强制等待
    def sleep_wait(self,num):
        time.sleep(num)

    #判断是否登陆成功
    def isloginsuccess(self,elem):
        flag=True
        try:
            self.driver.find_element_by_xpath(elem)
            print("登陆成功")
            return flag
        except:
            flag=False
            print("登陆失败")
            return flag
    #判断元素是否创建成功
    def mkdir_success(self,elem):
        if self.driver.find_element_by_xpath(elem):
            print("创建成功")
        else:
            print("创建失败")

    #判断清除元素是否成功
    def del_success(self,elem):
        if self.Find_element(elem):
            print("删除失败")
        else:
            print("删除成功")
    #判断元素是否存在
    def is_exist(self,elem):
        if self.driver.find_element_by_xpath(elem):
            print(self.driver.find_element_by_xpath(elem).text)
        else:
            return True



    #获取EOMS验证码输入并点击登陆
    def get_logincode(self,input_elem,login_elem,success_elem):
        path = 'D://taoler/pic'
        try:
            # 清空该文件夹内容
            for i in os.listdir(path):
                path_file = os.path.join(path, i)
                if os.path.isfile(path_file):
                    os.remove(path_file)
                else:
                    for f in os.listdir(path_file):
                        path_file2 = os.path.join(path_file, f)
                        if os.path.isfile(path_file2):
                            os.remove(path_file2)
            self.driver.save_screenshot("D://taoler/pic/01.png")  # 截取屏幕内容，保存到本地
            # time.sleep(5)
            ran = Image.open("D://taoler/pic/01.png")  # 打开截图，获取验证码位置，截取保存验证码
            # time.sleep(5)
            box = (985, 400, 1070, 450)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
            ran.crop(box).save("D://taoler/pic/02.png")  # 把获取的验证码保存
            # time.sleep(5)
            # 获取验证码图片，读取验证码
            imageCode = Image.open("D://taoler/pic/02.png")  # 打开保存的验证码图片
            imageCode.load()
            # 图像增强，二值化
            sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
            sharp_img.save("D://taoler/pic/03.png")  # 保存图像增强，二值化之后的验证码图片
            sharp_img.load()  # 对比度增强
            code =pytesseract.image_to_string(sharp_img).strip()  # 读取验证码
            #判断是否是数字
            code.isdigit()
            #输入验证码
            self.input_send_keys(input_elem,code)
            #点击登陆
            self.click(login_elem)
            #判断是否登陆成功
            loginin_success=self.get_text(success_elem)
            assert loginin_success=="欢迎您 : 管理员！"
            return code
        except:
            print("验证码获取失败，重新获取中")
            self.get_logincode(input_elem,login_elem,success_elem)




class Tkinter_windows(object):
    def test_inter(self,master):
        self.master=master
        self.master.title("粮达自动测试系统")  # 设置窗口标题
        self.master.geometry('480x500+10+10')  # 设置窗口大小，默认打开位置
        self.master.attributes("-alpha", 1.0)  # 设置窗口虚化程度

class log_input(object):
    def test_get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        return current_time














