from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("/html/body/div/form/div/div/div[1]/h2/img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("/html/body/div/form/div/div/input")
    input1.send_keys(y)

    option1 = browser.find_element_by_xpath("/html/body/div/form/div/div/div[2]/input[1]")
    option1.click()

    option2 = browser.find_element_by_xpath("/html/body/div/form/div/div/div[2]/input[3]")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("/html/body/div/form/div/div/button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()