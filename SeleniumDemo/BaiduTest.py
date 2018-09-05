#coding=utf-8
from selenium import webdriver
import time
def main():
    driver = webdriver.Chrome()
    first_url = r'http://www.baidu.com'
    second_url = r'http://cn.bing.com'
    driver.maximize_window()
    print("visit url : %s" %(first_url))
    driver.get(first_url)
    time.sleep(2)
    driver.find_element_by_id("kw").send_keys("hello")
    driver.find_element_by_id("su").click()
    time.sleep(2)
    print("visit url : %s" %(second_url))
    driver.get(second_url)
    time.sleep(2)
    print("visit url : %s" %(first_url))
    driver.back()
    time.sleep(2)
    print("visit url : %s" %(second_url))
    driver.forward()
    time.sleep(2)
    driver.quit()

if __name__=='__main__':
       main()