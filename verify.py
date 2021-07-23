import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    #link = "http://suninjuly.github.io/wait1.html"
    link = "http://suninjuly.github.io/wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    #time.sleep(2)
    # button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

finally:
    time.sleep(3)
    browser.quit()