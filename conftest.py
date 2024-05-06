import pytest
from selenium import webdriver
from data import User
from locators import LogInPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_driver(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*LogInPageLocators.email_input).send_keys(User.email)
    driver.find_element(*LogInPageLocators.password_input).send_keys(User.password)
    driver.find_element(*LogInPageLocators.login_button).click()
