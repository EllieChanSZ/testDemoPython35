from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://xueshu.baidu.com/")

#对话框div
# div = driver.find_element_by_class_name("index_topbanner")
# div.find_element_by_css_selector("#content > div > div.index_topbanner > span").click()
driver.find_element_by_id("kw").send_keys("hello")
# not-support-1
# driver.find_element_by_id("su").click()
# not-support-2
# ActionChains(driver).move_to_element(button).send_keys(Keys.ENTER)
# not-support-3
# ActionChains(driver).move_to_element(button).perform()
# not clickable at point (784, 217). Other element would receive the click: <a href
button = driver.find_element_by_id("su")
# solution 1
button.send_keys(Keys.ENTER)

time.sleep(2)
print(driver.current_url)
driver.quit()