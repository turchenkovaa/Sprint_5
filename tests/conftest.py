from selenium import webdriver
import pytest
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from data import Person
from expected_texts import BUN_TEXT, SAUCES_TEXT, TOPPINGS_TEXT


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_btn).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.login_account_btn).click()

    return driver