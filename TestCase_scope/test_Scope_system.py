#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
'''
_author_='Jianing'
_date_=21/11/30
_data_=''
order=1
'''
from LDW_Automate_POM.pages.element_Aloginpage import login_LDW_new
from LDW_Automate_POM.pages.element_scope_login import Scope_login
from selenium import webdriver
import pytest
class Test_scope():
    LDW_new_url=None
    LDW_new_name = "ceshi123"
    LDW_new_psw = "123456A@"
    @pytest.fixture(scope='function', autouse=True)
    def begin(self):
        self.driver = webdriver.Chrome()
        # yield
        # self.driver.quit()
    def test_scope_system(self):
        # 实例化登陆
        loginin_LDW_new = login_LDW_new(self.driver, self.LDW_new_url)
        loginin_LDW_new.login_ldw_new(self.LDW_new_name, self.LDW_new_psw)
        #进入权限界面
        login_scope=Scope_login(self.driver,self.LDW_new_url)
        login_scope.scope_login()
        login_scope.scope_exit()




