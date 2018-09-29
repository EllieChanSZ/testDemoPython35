# -*- coding: utf-8 -
import unittest
from PageObject.SearchPage import SearchPage
from selenium import webdriver
from time import sleep

class TestRun(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		sleep(2)
		self.driver.implicitly_wait(30)
		self.url = "http://www.baidu.com"
		sleep(2)
		self.content = "SearchText"

	def test_search(self):
		baidu_page = SearchPage(self.driver,self.url) #实例化SearchPage
		baidu_page.open() #SearchPage类的实例改写了open方法
		baidu_page.search_content(self.content)
		baidu_page.btn_click() #层层callback
		sleep(2)

	def tearDown(self):
		# pass
		self.driver.quit()

	if __name__ == "__main__":
		unittest.main()

