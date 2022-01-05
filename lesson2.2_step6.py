from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("/html/body/div/form/div[1]/label/span[2]")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input1.send_keys(y)

    option1 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
    option1.click()

    option2 = browser.find_element_by_xpath("/html/body/div/form/div[4]/input")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()