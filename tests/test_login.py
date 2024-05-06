from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LogInPageLocators, MainPageLocators, RegisterPageLocators
from data import User


class TestLogIn:

    #Вход по кнопке "Войти в аккаунт" на главной
    def test_login_by_button_on_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPageLocators.login_to_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))
        driver.find_element(*LogInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*LogInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*LogInPageLocators.login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    #Вход через кнопку "Личный кабинет"
    def test_login_by_personal_account_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))
        driver.find_element(*LogInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*LogInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*LogInPageLocators.login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    #Вход через кнопку в форме регистрации
    def test_login_by_registrashion_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*RegisterPageLocators.login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))
        driver.find_element(*LogInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*LogInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*LogInPageLocators.login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    #Вход через кнопку в форме восстановления пароля
    def test_login_by_password_recovery_form(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))
        driver.find_element(*LogInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*LogInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*LogInPageLocators.login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
