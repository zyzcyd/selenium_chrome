from read_init import ReadIni
from open_browser import selenium_webdriver
import time


read_ini = ReadIni()
data = read_ini.get_value('element', 'username')
data_info = data.split('>')
by = data_info[0]

selenium_driver = selenium_webdriver("chrome")

selenium_driver.get_url("https:\\www.baidu.com")
time.sleep(3)
selenium_driver.close_driver()