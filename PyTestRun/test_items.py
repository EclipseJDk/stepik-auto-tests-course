import time
from selenium.webdriver.common.by import By


def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_basket = browser.find_element(By.ID, "add_to_basket_form")
    time.sleep(4)
    assert add_to_basket.is_displayed(), "There is no button for adding an item to the cart "
