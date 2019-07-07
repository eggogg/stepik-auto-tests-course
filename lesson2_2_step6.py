from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_xpath("//label[@for=\"robotCheckbox\"]")
option1.click()
option2 = browser.find_element_by_xpath("//label[@for=\"robotsRule\"]")
option2.click()

# Ваш код, который заполняет обязательные поля
# Отправляем заполненную форму
button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
