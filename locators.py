from selenium.webdriver.common.by import By


class RegisterPageLocators: #Страница регистрации
    name_input = (By.XPATH, "//fieldset[1]/div/div/input")   #Поле ввода имени
    email_input = (By.XPATH, "//fieldset[2]/div/div/input")   #Поле ввода email
    password_input = (By.XPATH, "//fieldset[3]/div/div/input")   #Поле ввода пароля
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")   #Кнопка Зарегистрироваться
    incorrect_password =(By.XPATH, "//p[text()='Некорректный пароль']")   #Ошибка при вводе некорректного пароля
    login_button = (By.XPATH, "//a[@href='/login']")   #Кнопка "Войти"

class LogInPageLocators: #Страница входа
    login_button = (By.XPATH, "//button[text()='Войти']")   #Кнопка Войти
    email_input = (By.NAME, "name")   #Поле ввода email
    password_input = (By.NAME, "Пароль")   #Поле ввода пароля


class MainPageLocators: #Главная страница
    login_to_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")   #Кнопка "Войти в аккаунт"
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")   #Кнопка "Личный кабинет"
    place_order_button = (By.XPATH, "//button[text()='Оформить заказ']")   #Кнопка "Оформить заказ"
    sauces_section = (By.XPATH, "//span[text()='Соусы']")   #Раздел "Соусы"
    toppings_section = (By.XPATH, "//span[text()='Начинки']")   #Раздел "Начинки"
    buns_section = (By.XPATH, "//span[text()='Булки']")   #Раздел "Булки"
    active_section = (By.XPATH, "//div[contains(@class, 'current')]")

class PersonalAccountLocators:
    profile_button = (By.XPATH, "//a[@href='/account/profile']")   #Кнопка "Профиль"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")   #Кнопка "Конструктор"
    logo_stellar_burgers = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")   #Логотип StellarBurgers
    logout_button = (By.XPATH, "//button[text()='Выход']")   #Кнопка "Выход"