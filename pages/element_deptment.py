#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/10/20
_data_='创建和删除部门'
"""
from LDW_Automate_POM.pages.base import Base_pages
from selenium.webdriver.common.by import By
from selenium import webdriver
#创建和删除部门部门
class change_deptment(Base_pages):
    #展开折叠菜单
    open_menu=(By.XPATH,u'//*[@id="mainApp"]/div/div[2]/div[3]/i')
    #系统
    os_element=(By.XPATH,u'//*[@id="mainApp"]/div/div[2]/div[1]/div[1]/div/ul/li[2]/span')
    #系统中心-员工管理
    os_empioy=(By.XPATH,u'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/ul/li[1]/ul/li[1]/a/span')
    #组织框架-粮达网
    deptment_ldw=(By.XPATH,u'/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div')
    #组织架构—新建
    deptment_mkdir=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[3]/div/button[1]/i')
    #新增部门名称
    deptment_new_mkdir=(By.XPATH,u'/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[1]/input')
    deptment_name="自动生成部门"
    #新增部门确认按钮
    deptment_confirm=(By.XPATH,u"/html/body/div[2]/div/div[3]/div/button[2]/span")
    #若部门已存在提示
    deptment_exist=(By.XPATH,'//*[contains(text(),"重复")]')
    #新增部门取消按钮
    deptment_cancle=(By.XPATH,u'/html/body/div[2]/div/div[3]/div/button[1]/span')
    #获取已创建部门
    deptment_new=('//*[contains(text(),"自动生成部门")]')  #-----判断
    deptment_new_nomal=(By.XPATH,'//*[contains(text(),"自动生成部门")]')
    #搜索输入框
    deptment_new_enter=(By.XPATH,u'/html/body/div/div/div[3]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/input')
    #部门搜索
    deptment_new_soushuo=(By.XPATH,u'/html/body/div/div/div[3]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/span/span/i[1]')
    #删除部门
    deptment_del=(By.XPATH,u'/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div/button[3]/i')
    #确认删除部门
    deptment_del_enter=(By.XPATH,u'/html/body/div[3]/div/div[3]/div/button[2]/span')

    def __init__(self,driver,base_url):
        Base_pages.__init__(self,driver,base_url)
    #新建部门
    def mkdir_deptment(self):
        self.sleep_wait(3)
        self.click(self.open_menu)      #点开折叠菜单
        self.click(self.os_element)     #点击系统按钮
        self.click(self.os_empioy)      #点击员工管理
        self.sleep_wait(1)
        self.click(self.deptment_mkdir)  #点击粮达网下新建部门
        self.changes_handles(-1)
        self.sleep_wait(1)
        self.input_send_keys(self.deptment_new_mkdir,self.deptment_name)  #输入部门名称
        self.click(self.deptment_confirm)    #确认新建部门
        is_exist="部门名不允许重复，请重新输入！"
        try:
            if self.get_text(self.deptment_exist)==is_exist:  #判断部门是否重复
               print(self.get_text(self.deptment_exist))
               self.changes_handles(-1)
               self.sleep_wait(1)
               self.click(self.deptment_cancle)      #点击取消创建按钮
        except:
            self.sleep_wait(2)
        # 判断部门是否已经创建
        self.mkdir_success(self.deptment_new)
        # 删除部门
        self.input_send_keys(self.deptment_new_enter, self.deptment_name)  # 输入已创建部门
        self.click(self.deptment_new_soushuo)  # 搜索部门
        self.click(self.deptment_new_nomal)  # 点击该部门
        self.click(self.deptment_del)  # 点击删除部门
        self.changes_handles(-1)
        self.sleep_wait(2)
        self.click(self.deptment_del_enter)  # 确认删除部门
        # 删除输入框内容
        self.clear_input(self.deptment_new_enter)
        # 验证删除成功
        self.del_success(self.deptment_new)
















