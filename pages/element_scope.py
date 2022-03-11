#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
_author_='Jianing'
_date_=21/11/2
_data_='新增权限（权限测试角色）并删除其他权限组'


from LDW_Automate_POM.pages.base import Base_pages
from selenium.webdriver.common.by import By
#创建新的角色名称，全选所有权限
class Page_scope(Base_pages):
    # 新建角色名称
    rule_name = "权限测试角色"
    #当前登陆账户的名字
    loadname="sunjianing"
    # 展开折叠菜单
    open_menu = (By.XPATH, u'//*[@id="mainApp"]/div/div[2]/div[3]/i')
    # 系统
    os_element = (By.XPATH, u'//*[contains(text(),"系统")]')
    #角色权限管理
    os_scope=(By.XPATH,u'//*[contains(text(),"角色权限管理")]/..')
    #右上角角色
    now_user=(By.XPATH,u'/html/body/div/div/div[1]/div[2]/div/ul/li[1]/div[1]/span')
    #新建角色
    new_rule=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/button/span')
    #输入新建角色
    input_new_rule=(By.XPATH,u'/html/body/div[2]/div/div[2]/form/div/div/div[1]/input')
    #确认角色名称
    makesure_rulename=(By.XPATH,u'/html/body/div[2]/div/div[3]/div/button[2]/span')
    #判断角色名称是否存在
    rulername_isexist=(By.XPATH,u'//*[contains(text(),"已存在")]')
    #取消新建角色
    mkdirname_cancel=(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[1]/span')
    #判断是否创建成功
    rule_new = ('//*[contains(text(),self.rule_name)]')  # -----判断
    #搜索框输入新建的角色
    search_rulename=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/div[1]/input')
    #选择新创建的角色
    new_rulename=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/span')
    #关联员工
    relevance_rule=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[2]/div[1]/div[1]/div[2]/button/span')
    #选择当前登陆账户
    now_loadname=(By.XPATH,u'/html/body/div[3]/div/div[2]/form/div/div/div/div[1]/input')
    #下拉框中选择用户名
    loadname_text=(By.XPATH,u'/html/body/div[5]/div[1]/div[1]/ul/li')
    #下拉框显示无数据
    no_date=(By.XPATH,u'/html/body/div[5]/p')
    #若已关联无数据时取消关联员工
    chose_rulename_cancel=(By.XPATH,u'/html/body/div[3]/div/div[3]/div/button[1]/span')
    #消除下拉框人员列表
    cancel_rulename=(By.XPATH,u'/html/body/div[3]/div/div[1]')
    #确认选择关联角色
    makesure_loadname=(By.XPATH,u'/html/body/div[3]/div/div[3]/div/button[2]/span')
    #判断角色是否关联成功
    exist_relevance=('//*[@id="baseApp"]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div')
    #员工角色列表
    rule_list=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[3]/table/tbody/tr/td[5]/div')
    #点击搜索按钮
    search_rule=(By.XPATH,u'//*[@id="baseApp"]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/span')
    #权限移除按钮
    scope_remove=('//*[contains(text(),"sunjianing")]/../../td[6]/div/div/button/span')
    #确认移除权限按钮
    sure_delrulename=(By.XPATH,u'/html/body/div[5]/div/div[3]/div/button[2]/span')
    #验证删除其他权限
    sure_delotherrule=(By.XPATH,u'//*[contains(text(),self.loadname)]')
    #切换角色权限
    get_rule_scope=(By.XPATH,u'//*[@id="tab-2"]')
    #勾选所有功能权限
    all_scope=('//*[@id="baseApp"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div[1]/div/label/span[1]/input')
    #保存权限
    save_all_scope=(By.XPATH,u'/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/button/span')
    #添加成功
    success_addscope=(By.XPATH,u'//*[contains(text(),"功能权限成功")]')

    def change_scope_rulename(self):
        self.sleep_wait(1)
        self.click(self.open_menu)  # 点开折叠菜单
        self.click(self.os_element)  # 点击系统按钮
        self.click(self.os_scope)    #点击角色权限管理
        now_username=self.get_text(self.now_user)  #获取当前登录账户
        print("当前登陆账户名为：%s"% now_username)
        self.click(self.new_rule)      #新建角色
        self.input_send_keys(self.input_new_rule,self.rule_name)  #输入新建角色名称
        self.changes_handles(-1)
        self.sleep_wait(1)
        self.click(self.makesure_rulename)  # 确认新建角色名称
        is_exist="该角色名称已存在，请重新输入！"
        try:
            if self.get_text(self.rulername_isexist) in is_exist:  #判断角色是否重复
                print(self.get_text(self.rulername_isexist))
                self.sleep_wait(2)
                self.click(self.mkdirname_cancel)  # 点击取消创建按钮
        except:
            self.sleep_wait(1)
        self.mkdir_success(self.rule_new)   #判断是否创建成功
        self.sleep_wait(1)
        self.input_send_keys(self.search_rulename,self.rule_name)  #搜索输入新创建的角色名称
        self.click(self.new_rulename)    #选择新创建的角色
        self.click(self.relevance_rule)  #选择关联员工
        self.changes_handles(-1)
        self.sleep_wait(1)
        self.click(self.now_loadname)    #点击角色选择输入框
        self.input_send_keys(self.now_loadname,self.loadname)   #输入当前登陆员工姓名
        self.sleep_wait(1)
        self.changes_handles(-1)
        self.sleep_wait(1)
        is_rule="无数据"
        try:
            if self.get_text(self.no_date) in is_rule:     #当选择员工数据为空时
                print("角色已绑定过")
                self.click(self.cancel_rulename)         #点击标题框
                self.changes_handles(-1)
                self.sleep_wait(1)
                self.click(self.chose_rulename_cancel)   #点击取消关联员工
        except:
            self.click(self.loadname_text)    #点击下拉框中的用户名
            self.click(self.cancel_rulename)  #点击标题框
            self.changes_handles(-1)
            self.sleep_wait(1)
            self.click(self.makesure_loadname)              #确认选择角色名称
        self.mkdir_success(self.exist_relevance)            #确认关联成功
        rulenames=self.get_text(self.rule_list)             #获取角色列表
        rulenames_num=rulenames.split(",")                  #对角色列表进行切片
        rulenames_new_num=rulenames_num.index(self.rule_name)       #获取新建角色的list下标
        print("角色都有:"+rulenames)
        for i in range(len(rulenames_num)):
            if i ==rulenames_new_num:   #如果循环值与新增加的权限索引相同，则跳过
                pass
            else:
                self.input_send_keys(self.search_rulename, rulenames_num[i])  # 循环搜索对应的角色
                self.sleep_wait(2)
                self.click(self.search_rule)  # 点击对应角色
                self.js_click(self.scope_remove)  # 移除角色(子元素定位父元素方法)
                self.click(self.sure_delrulename)  #确认移除角色
                self.del_success(self.sure_delotherrule)  #判断元素是否删除成功
        print("角色权限唯一性添加成功")
        self.input_send_keys(self.search_rulename, self.rule_name)  # 搜索输入新创建的角色名称
        self.sleep_wait(1)
        self.click(self.new_rulename)  # 选择新创建的角色
        self.click(self.get_rule_scope)  #切换角色权限
        self.sleep_wait(2)
        if self.Find_elements(self.all_scope).is_selected():
            print("角色全选成功")
        else:
            self.js_click(self.all_scope)  # 点击全选
            self.click(self.save_all_scope)  # 保存权限

class Scope_login(Base_pages):
    #退出登陆按钮
    Confirm_exit=(By.XPATH,u'/html/body/div/div/div[1]/div[2]/div/ul/li[2]/i')
    #确认退出登陆
    sure_confirm_exit=(By.XPATH,u'/html/body/div[2]/div/div[3]/div/button[2]/span')


    #系统中心-员工管理-查看
    system_rule_view=('/html/body/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/table[1]/tr/td[2]/table/tr[1]/td[1]/label/span[1]/input')

    def scope_login(self):
        self.sleep_wait(2)
        self.click(self.system_rule_view)  #点击取消员工管理-查看按钮
        if self.Find_elements(self.system_rule_view).is_selected():
            self.click(self.system_rule_view)  # 点击取消员工管理-查看按钮
            print("取消选择员工管理-查看")
        else:
            pass
















