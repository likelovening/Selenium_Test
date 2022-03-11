#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from LDW_Automate_POM.pages.element_Aloginpage import  login_LDW_new
from LDW_Automate_POM.pages.element_deptment import change_deptment
import pytest
from selenium import webdriver
class Test_check_deptName():
    LDW_new_url = None
    LDW_new_name = "ceshi123"
    LDW_new_psw = "123456A@"
    @pytest.fixture(scope='function', autouse=True)
    def begin(self):
        self.driver = webdriver.Chrome()
        #yield
        #self.driver.quit()

    def test_check_mkdir_del_deptName(self):
        loginin_ldw_new = login_LDW_new(self.driver, self.LDW_new_url)
        # 登陆粮达网运营平台
        loginin_ldw_new.login_ldw_new(self.LDW_new_name, self.LDW_new_psw)
        #新增部门
        new_dept=change_deptment(self.driver, self.LDW_new_url)
        new_dept.mkdir_deptment()


