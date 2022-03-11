#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/10/20
_data_='封装登陆操作'
"""

from selenium import webdriver
from LDW_Automate_POM.pages.base import Base_pages
from selenium.webdriver.common.by import By
#登陆粮达网1.0
class login_LDW_old(Base_pages):
    #粮达网主页url
    LDW_url = 'http://test.liangdawang.com:8085/portal/'
    #主页请登陆按钮
    LDW_pls_login=(By.XPATH,u'/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]')
    #登陆界面用户名输入框
    LDW_user_name_element=(By.CLASS_NAME,u'ant-input')
    #登陆界面密码输入框
    LDW_user_psw_element=(By.XPATH,u'//input[contains(@placeholder,"密码")]')
    #登陆界面确认登陆
    LDW_enter_login=(By.XPATH,u'/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button')
    def __init__(self,driver,base_url):
        Base_pages.__init__(self,driver,base_url)
    #主页登陆
    def login_ldw(self,user_name,user_psw):
        self.driver.get(self.LDW_url)     #打开主页
        self.click(self.LDW_pls_login)    #点击请登陆按钮
        self.input_send_keys(self.LDW_user_name_element,user_name)   #LDW输入用户名
        self.input_send_keys(self.LDW_user_psw_element,user_psw)     #LDW输入密码
        self.click(self.LDW_enter_login)                             #确认登陆
#登陆EOMS
class login_EOMS(Base_pages):
    #EOMS登陆主页
    EOMS_url="http://test.eoms.liangdawang.com:8087/eoms/page/portalManage/login.jsp"
    #EOMS名字输入框
    EOMS_user_name_element=(By.XPATH,u'/html/body/div[2]/div/form/div[1]/input')
    #EOMS密码输入框
    EOMS_user_psw_element=(By.XPATH,u"//*[@id='pwdzone']")
    #EOMS验证码
    EOMS_Changecode_element=(By.XPATH,u'//*[@id="changeCode"]')
    #EOMS验证码输入框
    EOMS_Inputcode_element=(By.XPATH,u'//*[@id="codeInput"]')
    #EOMS确认登陆
    EOMS_enter_Login_element=(By.XPATH,u'//*[@id="form1"]/div[4]/a')
    #EOMS登陆后界面标题（判断是否登陆成功）
    EOMS_Login_title_element=(By.XPATH,u'//*[@id="logininfo"]')
    EOMS_Login_title=('//*[@id="logininfo"]')      #-----判断

    def __init__(self,driver,base_url):
        Base_pages.__init__(self,driver,base_url)
    #EOMS登陆
    def Login_eoms(self,user_name,user_psw):
        self.driver.get(self.EOMS_url)
        self.input_send_keys(self.EOMS_user_name_element, user_name)  # EOMS输入用户名
        self.input_send_keys(self.EOMS_user_psw_element, user_psw)  # EOMS输入密码
        self.click(self.EOMS_Changecode_element)                    #点击更换验证码图片
        # 输入验证码并验证登陆
        self.get_logincode(self.EOMS_Inputcode_element,self.EOMS_enter_Login_element,self.EOMS_Login_title_element)
        self.sleep_wait(2)
        self.isloginsuccess(self.EOMS_Login_title)
#粮达网2.0运营平台登陆
class login_LDW_new(Base_pages):
    #粮达网2.0运营中心
    LDW_operation_url="https://stg.liangdawang.com:8096/login"
    #粮达网2.0运营中心主页用户名输入框
    LDW_operation_user_name=(By.XPATH,u"/html/body/div[1]/div/form/div[2]/div/div/input")
    #粮达网2.0运营中心主页密码输入框
    LDW_operation_user_psw=(By.XPATH,u'/html/body/div[1]/div/form/div[3]/div/div/input')
    #粮达网2.0运营中心主页登录
    LDW_new2_login=(By.XPATH,u'/html/body/div[1]/div/form/button/span')
    #粮达网2.0运营平台主页登陆密码错误
    LDW_new2_login_error=(By.XPATH,u'/html/body/div[3]/p')
    #粮达网2.0运营平台主页logo（判断是否登陆成功）
    LDW_new2_login_success=(u'/html/body/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/span')     #-----判断

    def __init__(self,driver,base_url):
        Base_pages.__init__(self,driver,base_url)
    #粮达网2.0运营平台登陆
    def login_ldw_new(self,user_name,user_psw):
        self.driver.get(self.LDW_operation_url)                         #打开url
        self.input_send_keys(self.LDW_operation_user_name,user_name)    #输入账户
        self.input_send_keys(self.LDW_operation_user_psw,user_psw)      #输入密码
        self.click(self.LDW_new2_login)                                 #点击登陆
        self.sleep_wait(2)
        self.isloginsuccess(self.LDW_new2_login_success)                #判断是否登陆成功




