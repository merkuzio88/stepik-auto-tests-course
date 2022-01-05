from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_id("button")
    button1.click()

finally:
    time.sleep(10)

    browser.quit()