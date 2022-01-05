from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath("/html/body/form/div/div/div/label/span[2]")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath("/html/body/form/div/div/div/input")
    input1.send_keys(y)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()

    time.sleep(1)

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(10)

    browser.quit()