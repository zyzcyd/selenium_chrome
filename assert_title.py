import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"/Users/zhangjiangtao/Python/chromedriver/chromedriver")
driver.get('https://www.imooc.com')
title = driver.title
print(title)


title_a = EC.title_is('慕课网')
print(title_a(driver))

title_b = EC.title_contains('慕课网')
print(title_b(driver))

driver.close()

