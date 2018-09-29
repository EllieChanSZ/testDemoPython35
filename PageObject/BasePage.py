from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
class BasePage(object):

	"""
	BasePage封装了所有页面的公共方法，比如driver，find_element等
	实例化BasePage类时，最先执行__init__方法，init方法不能有返回值
	init方法的参数就是BasePage的入参
	"""
	def __init__(self,selenium_driver,base_url):
		self.driver = selenium_driver #实例化
		self.base_url = base_url

	def on_page(self,page_title):
		return page_title in self.driver.title

	def _open(self,url):
		self.driver.get(url)
		self.driver.maximize_window()

	def open(self):
		self._open(self.base_url,self.page_title)

	# Locate Web Element
	# *loc 任意数量的位置参数
	def find_element(self,*loc):
		try:	#等待10秒
			WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
			return self.driver.find_element(*loc)
		except:
			print("%s 页面未能查找到 %s 元素" %(self,loc))

	#调用JS代码
	def script(self,src):
		self.driver.execute_script(src)

	def send_keys(self,loc,value,clear_first=True,click_first=True):
		try:
			loc = getattr(self," %s"%loc) #getattr相当于实现了self.loc
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				#先清空后赋值
				self.find_element(*loc).clear()
				self.find_element(*loc).send_keys(value)
		except AttributeError:
			print("%s 页面未能查找到 %s 元素" % (self, loc))
