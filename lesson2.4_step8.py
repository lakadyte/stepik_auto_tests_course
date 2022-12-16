from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
import os 


link = "http://suninjuly.github.io/explicit_wait2.html"
   
try:
   
    browser = webdriver.Chrome()
    browser.get(link)
    
    wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #selenium.webdriver.support.expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
    
    btn = browser.find_element(By.ID, "book").click() 
    
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
   
    butSubmit = browser.find_element(By.ID, 'solve')
    butSubmit.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()