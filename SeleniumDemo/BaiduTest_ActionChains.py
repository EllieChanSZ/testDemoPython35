#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
def main():
    driver = webdriver.Chrome()
    first_url = r'http://www.baidu.com'
    driver.get(first_url)
    driver.find_element_by_id("kw").send_keys("hello")
    time.sleep(0.3)
    print (os.path.basename('BaiduTest.py'))
    button = WebDriverWait(driver, 10).until(lambda e: e.find_element_by_id("su"))

    actions_chains = ActionChains(driver)
    actions_chains.move_to_element(button).click()
    driver.get(first_url)
    driver.find_element_by_id("kw").send_keys("world!")
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
    driver.implicitly_wait(3)
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
    time.sleep(3)
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
    time.sleep(3)
    driver.find_element_by_id("kw").send_keys(Keys.ENTER)
    driver.quit()

if __name__=='__main__':
       main()
       print ("done!")