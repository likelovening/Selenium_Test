#!/usr/bin/evn python
# -*- encoding: utf-8 -*-

import unittest
import pytest
import sys
from selenium import webdriver
from LDW_Automate_POM.pages.element_Aloginpage import  login_LDW_old,login_EOMS,login_LDW_new
from LDW_Automate_POM.pages.element_kxxreport import KXXreport

class Test_KXXreport():
    LDW_url = None
    user_ywy_name = "ldwywy"
    user_ywy_psw = "123456"
    EOMS_url = None
    user_EOMS_name = "admin"
    user_EOMS_psw = "dajidali"
    LDW_new_url=None
    LDW_new_name="sjn123456"
    LDW_new_psw="123456A@"
    #@pytest.mark.skip()
    @pytest.fixture(scope='function', autouse=True)
    def begin(self):
        self.driver = webdriver.Chrome()

    def test_loginin_ldw(self):
        loginin_ldw=login_LDW_old(self.driver,self.LDW_url)
        #调用登陆主页
        loginin_ldw.login_ldw(self.user_ywy_name,self.user_ywy_psw)
        #设置可行性报告填写
        kxxreport_input=KXXreport(self.driver,self.LDW_url)
        kxxreport_input.input_js_report()
        #self.driver.quit()

    #@pytest.mark.skip()
    def test_loginin_EOMS(self):
        loginin_eoms=login_EOMS(self.driver,self.EOMS_url)
        #调用登陆EOMS
        loginin_eoms.Login_eoms(self.user_EOMS_name,self.user_EOMS_psw)

    def test_loginin_LDW_new(self):
        loginin_ldw_new=login_LDW_new(self.driver,self.LDW_new_url)
        #调用登陆粮达网运营平台
        loginin_ldw_new.login_ldw_new(self.LDW_new_name,self.LDW_new_psw)




if __name__=="__main__":
    pytest.main(['-s', '--tests-per-worker=3', '--html=xdist2.html', '--self-contained-html',  __file__])






