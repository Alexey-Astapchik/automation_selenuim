from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exist(browser):
    browser.get(link)
    basket_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert basket_button.size != 0, "Button does not exist."
    time.sleep(5)
