import pytest
import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
	browser.get(link)
	button_add_to_busket = browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

	assert len(button_add_to_busket) > 0, f"Button add to busket is not found: {button_add_to_busket}"