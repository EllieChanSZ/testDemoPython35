from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

print("1")
link = driver.find_element_by_link_text("设置").click()
print("2")
driver.find_element_by_link_text("搜索设置").click()
print("3")
driver.find_element_by_class_name("prefpanelgo").click()
alert = driver.switch_to_alert()
text = alert.text
print(text)
alert.accept()

driver.quit()
