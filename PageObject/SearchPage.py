#coding=utf-8
# 优化前场景
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com')
# driver.find_element_by_xpath(".//input[@id='kw']").send_keys("ellie")
# driver.find_element_by_xpath(".//input[@id='su']").click()
# sleep(3)
# driver.quit()

#优化后场景
from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage): #继承Base基类
	# 定位元素-变量提升，只改这一处
	search_loc = (By.ID,"kw")
	btn_loc = (By.ID,"su")
	# 重写
	def open(self):
		self._open(self.base_url)
	def search_content(self,content):
		content_value = self.find_element(*self.search_loc)
		content_value.send_keys(content)
	def btn_click(self):
		BaiduBtn = self.find_element(*self.btn_loc)
		BaiduBtn.click()

