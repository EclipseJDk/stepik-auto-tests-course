import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    input1 = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    num = calc(input1)
    answer.send_keys(num)
    solve = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    solve.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[1])

finally:
    time.sleep(10)
    browser.quit()
