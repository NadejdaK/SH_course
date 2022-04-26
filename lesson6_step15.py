from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math 

# Математическая функция
def sum(x,y):
   return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #находим элемент, содержащий значение для переменной x
    x_element = browser.find_element_by_id("num1")
    # записываем в переменную х текст из элемента x_element
    x=x_element.text
    
    #находим элемент, содержащий значение для переменной y
    y_element = browser.find_element_by_id("num2")
    # записываем в переменную y текст из элемента y_element
    y=y_element.text
    
    # Считаем математическую функцию
    z=sum(x,y)
    
        
    # Находим и раскрываем список
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(value=str(z)) 
        
     #Нажать на кнопку Submit
    
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()