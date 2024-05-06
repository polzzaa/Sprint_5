from healpers import get_sign_up
from locators import RegisterPageLocators, LogInPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistrationPage:
    #Проверка регистрации пользователя
    def test_registration_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        name_data, email_data, password_data = get_sign_up()
        driver.find_element(*RegisterPageLocators.name_input).send_keys(name_data)
        driver.find_element(*RegisterPageLocators.email_input).send_keys(email_data)
        driver.find_element(*RegisterPageLocators.password_input).send_keys(password_data)
        driver.find_element(*RegisterPageLocators.registration_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    #Ошибка для некорректного пароля
    def test_registration_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        name_data, email_data, password_data = get_sign_up()
        driver.find_element(*RegisterPageLocators.name_input).send_keys(name_data)
        driver.find_element(*RegisterPageLocators.email_input).send_keys(email_data)
        driver.find_element(*RegisterPageLocators.password_input).send_keys('1234')
        driver.find_element(*RegisterPageLocators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.incorrect_password))
        error = driver.find_element(*RegisterPageLocators.incorrect_password).text
        assert error =='Некорректный пароль'