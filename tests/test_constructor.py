from locators import MainPageLocators


class TestConstructor:

    #Переход к разделу "Соусы"
    def test_move_to_sauces_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPageLocators.sauces_section).click()

        assert driver.find_element(*MainPageLocators.active_section).text == 'Соусы'


    #Переход к разделу "Начинки"
    def test_move_to_toppings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPageLocators.toppings_section).click()

        assert driver.find_element(*MainPageLocators.active_section).text == 'Начинки'


    #Переход к разделу "Булки"
    def test_move_to_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPageLocators.toppings_section).click()
        driver.find_element(*MainPageLocators.buns_section).click()

        assert driver.find_element(*MainPageLocators.active_section).text == 'Булки'
