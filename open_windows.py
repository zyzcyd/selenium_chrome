from selenium import webdriver
import time
from open_browser import selenium_webdriver as sw
from read_init import read_ini
# from selenium.webdriver.support import expected_conditions as EC




# driver = webdriver.Chrome(r"/Users/zhangjiangtao/Python/chromedriver/chromedriver")
# driver.get("https://www.imooc.com/user/newlogin")
# driver.find_element_by_name('email').send_keys('zcyd_zy@163.com')
# driver.find_element_by_name('password').send_keys('123456789.')
# driver.find_element_by_class_name('moco-btn').click()
# time.sleep(2)
#
# driver.get('https://www.imooc.com/user/setbindsns')
# driver.find_elements_by_class_name('inner-i-box')[1].find_element_by_class_name('moco-btn-normal').click()
# handl_list = driver.window_handles
# current_handle = driver.current_window_handle
# print(handl_list)
# #[1,2,3,4]
# time.sleep(15)
# for i in handl_list:
#     if i != current_handle:
#         time.sleep(2)
#         driver.switch_to.window(i)
#         ti = EC.title_contains("网站连接")
#         if ti(driver) == True:
#             break
# time.sleep(5)
# driver.find_element_by_id('userId').send_keys('test')
# time.sleep(5)
# driver.close()
#
# driver.find_element_by_name("1").is_displayed()
# # 自动定位可以直接输入
selenium_driver = sw("chrome")
selenium_driver.get_url('https://www.imooc.com/user/newlogin')
# element = selenium_driver.get_element('element', 'username')
# print(element)
# selenium_driver.send_value('test', "element", 'username')
# selenium_driver.send_value('test', "element", 'password')
selenium_driver.check_box_is_selected(False, 'element', 'check_box')
time.sleep(5)
# selenium_driver.close_driver()


