import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_card_btn(browser):
    browser.get(link)
    add_to_basket = browser.find_elements(By.ID, "add_to_basket_form")
    time.sleep(4)
    assert add_to_basket, "There is no button for adding an item to the cart "
