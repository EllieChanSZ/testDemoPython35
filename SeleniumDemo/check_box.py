from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
path = os.path.abspath('checkbox.html')
driver.get('file:///' + path.__str__())
list = driver.find_elements_by_tag_name('input')
for i in list:
	if i.get_attribute('type') == 'checkbox':
		print(i.get_attribute('id'))
		i.click()
time.sleep(2)
try:
	element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('cb1'))
except:
	print('throw exception')
	driver.quit()
print(element)
driver.quit()
