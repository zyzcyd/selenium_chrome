from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from read_init import read_ini


class selenium_webdriver():

    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def open_browser(self, browser):
        '''
        打开浏览器驱动
        :param browser: 浏览器类型Chrome、firefox、IE
        :return: webdriver
        '''
        if browser == "chrome":
            driver = webdriver.Chrome(r"/Users/zhangjiangtao/Python/chromedriver/chromedriver")
        else:
            driver = None
        return driver

    def get_url(self, url):
        '''
        判断链接是否正确
        :param url: 要进入的链接
        '''
        if self.driver != None:
            time.sleep(1)
            self.driver.maximize_window()
            if 'http' in url:
                self.driver.get(url)
            elif 'D' in url:
                self.driver.get(url)
            else:
                print("你的URL有问题")
        else:
            print("case失败")
        # self.driver.quit()

    def handle_windows(self, *args):
        '''
        控制浏览器大小
        :param args: 1/2个参数
        :maximize_window:   窗口最大化
        :minimize_window:   窗口最小化
        :set_window_size(x,y):改变窗口的固定大小
        :back:    返回上一页
        :onward:    下一页
        :refresh:   刷新页面
        '''
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print("你传递的参数有问题")
        time.sleep(5)
        self.driver.quit()

    def assert_title(self, title_name=None):
        '''
        判断浏览器打开的页面是否正确
        :param title_name: 需要检验的页面title
        :return:
        '''
        if title_name is not None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self, url, title_name=None):
        '''
        判断打开的链接是否正确，并打开浏览器
        :param url: 要打开的链接
        :param title_name: 判断页面的title名称
        :return: True or False
        '''
        self.get_url(url)
        return self.assert_title(title_name)

    def close_driver(self):
        self.driver.close()

    def swich_windows(self, title_name=None):
        '''
        判断页面并进行切换
        :param title_name: 要切换的正确页面的title
        :return:
        '''
        handl_list = self.driver.window_handles  # 获取所有Table页面，并生成列表
        current_handle = self.driver.current_window_handle  # 当前窗口
        for i in handl_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)  # 切换窗口至i的table页
                if self.assert_title(title_name):
                    break

    def get_element(self, info):
        '''
        定位元素
        :param by:
        :param value:
        :return:
        '''
        element = None
        by, value = self.get_local_element(info)
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == "css":
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            else:
                element = self.driver.find_element_by_xpath(value)
        except Exception as e:
            print("执行gel_element发生错误", e)
            print("定位方式：", by, "定位元素：", value, "没有找到对应的元素")
        return self.element_is_display(element)

    def get_elements(self, info):
        '''
        获取定位元素列表
        :param by:
        :param value:
        :return:
        '''
        elements = None
        element_list = []
        by, value = self.get_local_element(info)
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == 'class':
            elements = self.driver.find_elements_by_class_name(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
        for element in elements:
            if self.element_is_display(element):
                continue
            else:
                element_list.append(element)
        return element_list

    def get_level_element(self, info):
        '''
        获取定位元素列表中的层级定位元素
        :param by:要获取父级的元素方法
        :param value:要获取父级元素的名称
        :param node_by:要在父级元素中获取子集元素的方法
        :param node_value:要在父级元素中获取子集元素的名称
        :return:反馈已经定位到的元素内容
        '''
        element = self.get_element(info[:2])
        # 判断父级元素是否存在
        if element:
            print('父级元素查询错误')
            return False
        node_by,node_value = self.get_local_element(info[2:])
        if node_by == 'id':
            node_element = element.find_element_by_id(node_by)
        elif node_by == 'name':
            node_element = element.find_element_by_name(node_value)
        elif node_by == 'css':
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == 'class':
            node_element = element.find_element_by_class_name(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)

        return self.element_is_display(node_element)

    def element_is_display(self, element):
        '''
        判断所查找的元素是否可见
        :return:
        '''
        if element.is_displayed():
            return element
        else:
            return False

    def get_list_element(self, index, info):
        '''
        获取元素列表，并通过下标的方式定位元素
        :param by: 定位列表元素的方法
        :param value: 定位列表元素的名称
        :param index: 元素列表中要获取的元素的下标数据
        :return: 返回已经定位好的元素
        '''
        # print("---------------------")
        # print('get_list_element info :', info)
        elements = self.get_elements(info)
        if len(elements)==0:
            print('查找的元素列表为空')
        else:
            if len(elements) < index:
                return None
            else:
                return elements[index]

    def send_value(self, key, info):
        '''
        输入值
        :param by:
        :param value:
        :param key:
        :return:
        '''
        element = self.get_element(info)
        # print("element:", element)
        if element==False:
            print("输入失败，定位没有展现出来。")
        else:
            if element is not None:
                print('------>')
                element.send_keys(key)
            else:
                print('输入元素类型没有找到')

    def click_element(self, info):
        '''
        点击定位元素
        :param by:
        :param value:
        :return:
        '''
        element = self.get_element(info)
        if element != False:
            element.click()
            # print("点击元素类型没有找到")
        else:
            print("点击元素类型没有找到")

    def check_box_is_selected(self, info, is_check=None):
        '''
        判断多元框是否选中以及是否需要选中，如果需要选中则is_check = True 如果不需要选中 is_check = False
        :param info:
        :param is_check:
        :return:
        '''

        if info is None:
            info = []
        element = self.get_element(info)
        # by, value = self.get_local_element(info)
        print('element', element)
        if element==False:
            print('点击元素不可见')
        else:
            flag = element.is_selected()
            print('flag:', flag)
            if flag:
                if is_check is not True:
                    self.click_element(info)
            else:
                if is_check:
                    self.click_element(info)

    def get_local_element(self, info):
        # print(info)
        '''
        读取配置文件
        :param info:要求传入元组 配置list&配置名称
        :return: 返回by 和 value
        '''
        data = read_ini.get_value(info[0], info[1])
        # print(data)
        return data.split('>')

    def selecter_element(self, info, value_index, index=None, ):
        selected_element = None
        if info is not None:
            selected_element = self.get_list_element(index, info)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)
