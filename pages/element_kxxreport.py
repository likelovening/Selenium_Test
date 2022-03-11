#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/10/20
_data_='元素合集、封装登陆操作'
"""
from selenium import webdriver
from LDW_Automate_POM.pages.base import Base_pages
from selenium.webdriver.common.by import By


class KXXreport(Base_pages):
    #主页我的粮达
    LDW_myld = (By.XPATH,u'/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a')
    #我的粮达
    LDW_myld_my=(By.XPATH,u'/html/body/div[3]/div/ul/li[1]/a')
    #选择寄售报告填写
    LDW_JS_report=(By.XPATH,u'//*[@id="MENU0105"]')
    #选择委托方信息
    LDW_chose_comp=(By.XPATH,u'/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/a/span[1]')
    #选择委托方公司
    LDW_chose_input=(By.XPATH,u'/html/body/div[9]/div/input')
    #公司名称
    LDW_Company_name="感动哈"
    #确认选择公司
    LDW_ENTER_COMP=(By.XPATH,u"/html/body/div[9]/ul/li/div")


    def __init__(self,driver,base_url):
        Base_pages.__init__(self,driver,base_url)
    #主页登陆
    def input_js_report(self):
        self.sleep_wait(5)
        self.click(self.LDW_myld)      #点击我的粮达
        self.sleep_wait(1)             #休眠1秒
        self.changes_handles(1)        #切换界面
        self.click(self.LDW_myld_my)   #进入我得粮达界面
        self.click(self.LDW_JS_report)     #选择寄售可行性报告填写
        self.sleep_wait(2)
        self.click(self.LDW_chose_comp)       #选择委托人列表
        self.input_send_keys(self.LDW_chose_input,self.LDW_Company_name)   #输入委托人信息
        self.click(self.LDW_ENTER_COMP)  #选择委托人公司











