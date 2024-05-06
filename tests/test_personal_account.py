from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, PersonalAccountLocators, LogInPageLocators


class TestPersonalAccount:

    #Переход по клику на «Личный кабинет»
    def test_click_on_personal_account_button(self, driver, login_driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.profile_button))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


    #Переход по клику на «Конструктор»
    def test_click_on_constructor_button(self, driver, login_driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.profile_button))
        driver.find_element(*PersonalAccountLocators.constructor_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    #Переход по клику на логотип Stellar Burgers
    def test_click_on_logo_stellar_burgers(self, driver, login_driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.profile_button))
        driver.find_element(*PersonalAccountLocators.logo_stellar_burgers).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    #Выход по кнопке «Выйти» в личном кабинете
    def test_click_on_logout_button(self, driver, login_driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.place_order_button))
        driver.find_element(*MainPageLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.profile_button))
        driver.find_element(*PersonalAccountLocators.logout_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LogInPageLocators.login_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'