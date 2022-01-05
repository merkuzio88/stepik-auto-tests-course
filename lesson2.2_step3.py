from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_x = browser.find_element_by_xpath("/html/body/div/form/h2/span[2]")
    x = int(element_x.text)

    element_y = browser.find_element_by_xpath("/html/body/div/form/h2/span[4]")
    y = int(element_y.text)

    z = x + y

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(z))


    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()