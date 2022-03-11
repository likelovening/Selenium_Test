#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from LDW_Automate_POM.pages.base import Base_pages
from selenium.webdriver.common.by import By

class Scope_login(Base_pages):
    # 角色名称
    rule_name = "权限测试角色"
    # 展开折叠菜单
    open_menu = (By.XPATH, u'//*[@id="mainApp"]/div/div[2]/div[3]/i')
    # 系统
    os_element = (By.XPATH, u'//*[contains(text(),"系统")]')
    # 角色权限管理
    os_scope = (By.XPATH, u'//*[contains(text(),"角色权限管理")]/..')
    #输入框输入权限测试角色
    search_rulename=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/div[1]/input')
    # 选择权限测试角色
    new_rulename = (By.XPATH, u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div')
    # 切换角色权限
    get_rule_scope = (By.XPATH, u'//*[contains(text(),"角色权限")]')

    #退出登陆按钮
    Confirm_exit=(By.XPATH,u'/html/body/div/div/div[1]/div[2]/div/ul/li[2]/i')
    #确认退出登陆
    sure_confirm_exit=(By.XPATH,u'/html/body/div[2]/div/div[3]/div/button[2]/span')
    #退出后的标题
    exit_title=('/html/body/div[1]/div/form/div[1]/div[1]')

    def scope_login(self):
        self.sleep_wait(1)
        self.click(self.open_menu)  # 点开折叠菜单
        self.click(self.os_element)  # 点击系统按钮
        self.click(self.os_scope)  # 点击角色权限管理
        self.sleep_wait(2)
        self.input_send_keys(self.search_rulename,self.rule_name)  #输入框搜索角色
        self.click(self.new_rulename)   #点击搜索的角色
        self.click(self.get_rule_scope) #却换角色权限
        print('角色权限界面打开成功')

    def scope_exit(self):
        self.sleep_wait(1)
        self.click(self.Confirm_exit)   #点击退出登陆按钮
        self.click(self.sure_confirm_exit)  #确认退出登陆按钮
        self.isloginsuccess(self.exit_title)  #确认已经退出登陆
        print("退出登陆成功")




