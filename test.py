from open_browser import selenium_webdriver

driver = selenium_webdriver("chrome")

driver.selecter_element(1, ['key', 'value'])

driver.close_driver()