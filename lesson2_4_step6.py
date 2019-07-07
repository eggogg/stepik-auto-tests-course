from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
browser.get(link)

button = browser.find_element_by_id("button")
button.click()
