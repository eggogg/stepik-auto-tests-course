from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button = browser.find_element_by_id("book")
button.click()
browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_id("solve")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
