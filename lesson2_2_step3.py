from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)
sum = num1 + num2

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(sum)) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
#time.sleep(1)

