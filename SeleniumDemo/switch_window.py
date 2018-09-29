from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://xueshu.baidu.com/")

nowhandle = driver.current_window_handle
print('homepage:' + nowhandle)

ele = WebDriverWait(driver, 10).until(lambda e: e.find_element_by_css_selector("#u > a.reg"))
ele.click()
time.sleep(3)

all_handles = driver.window_handles

for handle in all_handles:
	print('now:' + handle)
	print(len(all_handles))
	if handle != nowhandle:
		print('process...')
		driver.switch_to_window(handle)
		user = driver.find_element_by_name("userName")
		user.send_keys("userName")
		psd = driver.find_element_by_id("TANGRAM__PSP_3__password")
		psd.send_keys("password")

		time.sleep(2)
		print('backward')
		driver.switch_to_window(nowhandle)
		driver.find_element_by_id("kw").send_keys("hello")
		float_it = driver.find_element_by_class_name("index_topbanner")
		float_it.find_element_by_css_selector("#content > div > div.index_topbanner > span").click()
		hover_it = driver.find_element_by_id("su")
		hover_it.click()
		# ActionChains(driver).move_to_element(hover_it).click()
		title = driver.title
		print(title + ":" + driver.current_url)
		time.sleep(10)
driver.close()
driver.quit()
