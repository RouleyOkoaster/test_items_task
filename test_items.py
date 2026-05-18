import pytest
from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    button=browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button)==1, "Button either isn't present or theres more than one with that selector"
