#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import unittest
from LDW_Automate_POM.TestCase.test_Aloginin_func import Test_KX_jishou
if __name__=="__main__":
    testui=unittest.TestSuite()
    testui.main(Test_KX_jishou('KX_js'))








