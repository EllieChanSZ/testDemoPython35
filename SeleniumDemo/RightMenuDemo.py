# -*- coding: utf-8 -*-
import os
import os.path
import time
import win32api
import win32con

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 查找文件是否存在
def is_file_existed(filename):
    if os.path.exists(filename):
        print('Exe found Success')
        return True
    else:
        print('File not existed')
        return False

def main():
    driver = webdriver.Chrome()
    homeurl = r'https://www.autoitscript.com'

    try:
        driver.get(homeurl)
        link1 = driver.find_element_by_xpath("//*[@id='menu-item-207']")
        link2 = driver.find_element_by_xpath("//*[@id='menu-item-209']/a")

        actions = ActionChains(driver)
        actions.move_to_element(link1)
        actions.click(link2)
        actions.perform()
        # link2.click()
        time.sleep(10)
        # roll and click for download
        link3 = driver.find_element_by_xpath(".//*[@id='post-77']/div/table[2]/tbody/tr[1]/td[2]/a/img")
        driver.execute_script("arguments[0].scrollIntoView(true);", link3)
        actions_chains = ActionChains(driver)
        actions_chains.move_to_element(link3)
        actions_chains.context_click(link3).perform()
        time.sleep(2)
        # actions_chains.context_click(link3).send_keys(Keys.ARROW_DOWN)
        # time.sleep(1)
        # actions_chains.context_click(link3).send_keys(Keys.ARROW_DOWN)
        # time.sleep(1)
        # actions_chains.context_click(link3).send_keys(Keys.ARROW_DOWN)
        # time.sleep(1)
        # actions_chains.context_click(link3).send_keys(Keys.ARROW_DOWN)
        # time.sleep(1)
        # actions_chains.context_click(link3).send_keys(Keys.ENTER)
        win32api.keybd_event(40, 0, 0, 0)
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

        win32api.keybd_event(40, 0, 0, 0)
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

        win32api.keybd_event(40, 0, 0, 0)
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

        win32api.keybd_event(40, 0, 0, 0) # down
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0) # down释放
        time.sleep(2)
        win32api.keybd_event(13, 0, 0, 0)  # enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    except TimeoutException:
        print('TimeOut')
    except IOError:
        print('IOError')
    # except NameError:
    #             print ('NameError')

    file_name = r'C:\gts\DData\seleniumdemo\chromedownload.exe'
    download_file = r'C:\gts\DData\seleniumdemo\autoit-v3-setup.exe'
    if is_file_existed(download_file):
        os.remove(download_file) #remove previous download file
    if is_file_existed(file_name):
        print("start to callback script:")
        os.system(file_name)
    else:
        driver.quit()
        raise "Script not found!"

    # leave time for download big size file
    while not is_file_existed(download_file):
        time.sleep(10)
    print("file [%s] download success" %(download_file))
    driver.quit()

if __name__ == '__main__':
    main()



