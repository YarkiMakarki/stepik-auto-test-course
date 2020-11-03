from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = browser.find_element_by_css_selector("#input_value")
    x = int(num.text)
    y = calc(x)
    s = str(y)
    pole = browser.find_element_by_css_selector("#answer")
    pole.send_keys(s)

    button2 = browser.find_element_by_tag_name("button")
    button2.click()



finally:
    time.sleep(10)
    browser.quit()