import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium import webdriver.Chrome
#from selenium import webdriver.ChromeOptions
driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
wait=WebDriverWait(browser, 3)

browser.get(r'C:\gts\DData\seleniumdemo\readonly.html')
input = wait.until(
            EC.presence_of_element_located((By.ID, 'id1'))
        )

input1 = browser.find_element_by_id('id1')

input1.send_keys("hellow@163.com")
input2 = wait.until(
            EC.presence_of_element_located((By.ID, 'id2'))
        )
# #remove readonly attribute
#input2.removeAttribute('readonly');

browser.execute_script("arguments[0].setAttribute('name', arguments[1]);",input2,"chenjiayun");
browser.execute_script("arguments[0].removeAttribute('readonly');",input2);
input2.send_keys("ellie")
browser.execute_script("window.alert('ellie')");
# submit = wait.until(
#              EC.element_to_be_clickable(By.ID,'id3')
#         )
#submit = browser.find_element_by_id('id3')
#submit.click()