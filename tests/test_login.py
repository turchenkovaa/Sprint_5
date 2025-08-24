from data import Person
from locators import (
    MainPageLocators,
    AuthPageLocators,
    RegistrationPageLocators,
    RecoverPageLocators
)
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_in_login_btn_success(self, driver):
        # вход в личный кабинет на главной странице через кнопку "Войти в аккаунт" 

        driver.get(URLS.MAIN_PAGE_URL)  # открывается главная страница
        driver.find_element(*MainPageLocators.login_account_btn).click()           # нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)         # вводим email
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)        # вводим пароль
        driver.find_element(*AuthPageLocators.login_account_btn).click()          # нажимаем на кнопку входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )  # ожидание появления кнопки "Оформить заказ"
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text            # получаем текст кнопки
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')      # проверяем URL и текст

    def test_login_in_personal_account_btn_success(self, driver):
        # вход в личный кабинет на главной странице через кнопку "Личный кабинет" 

        driver.get(URLS.MAIN_PAGE_URL)     # открывается главная страница
        driver.find_element(*MainPageLocators.personal_account_btn).click()          # нажимаем на "Личный кабинет"
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_registration_form_success(self, driver):
        # вход в личный кабинет через форму регистрации

        driver.get(URLS.REG_PAGE_URL)       # открывается страница регистрации
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()         # нажимаем "Войти"
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_recover_form_success(self, driver):
        # вход в личный кабинет через форму восстановления

        driver.get(URLS.RECOVER_PAGE_URL)        # открывается страница восстановления
        driver.find_element(*RecoverPageLocators.login_account_btn).click()           # нажимаем кнопку "Войти"
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')