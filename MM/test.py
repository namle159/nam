from selenium.webdriver import Chrome
driver = Chrome()
driver.get('https://www.google.com/')
driver.find_element('name', 'q').send_keys('abc')