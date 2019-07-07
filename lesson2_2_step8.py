from selenium import webdriver
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_xpath("//input[@placeholder=\"Введите имя\"]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath("//input[@placeholder=\"Введите фамилию\"]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath("//input[@placeholder=\"Введите Email\"]")
input3.send_keys("me@test.com")

element = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)
   
# Ваш код, который заполняет обязательные поля
# Отправляем заполненную форму
button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
