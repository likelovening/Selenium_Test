#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from LDW_Automate_POM.pages.element_Aloginpage import login_LDW_new
from LDW_Automate_POM.pages.element_scope import Page_scope
from selenium import webdriver
import pytest
@pytest.fixture(scope='session', autouse=True)
def test_test():
    LDW_new_url = None
    LDW_new_name = "ceshi123"
    LDW_new_psw = "123456A@"
    driver = webdriver.Chrome()
    # 实例化登陆
    loginin_LDW_new = login_LDW_new(driver, LDW_new_url)
    loginin_LDW_new.login_ldw_new(LDW_new_name, LDW_new_psw)
    # 实例化新增唯一权限
    scope_fix = Page_scope(driver, LDW_new_url)
    scope_fix.change_scope_rulename()



