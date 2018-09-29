from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

print("1")
link = driver.find_element_by_link_text("设置").click()
print("2")
driver.find_element_by_link_text("高级搜索").click()
print("3")
driver.find_element_by_css_selector("select[name=\'gpc\']").click()
print("4")
driver.find_element_by_css_selector("#adv-setting-4 > select > option:nth-child(2)").click()

time.sleep(2)

driver.quit()
