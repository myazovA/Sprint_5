from locators import Locators

class TestMainPage:

    def test_main_sause_section_click_sause_shows(self, driver):

        driver.find_element(*Locators.MAIN_SAUSE).click()

        assert driver.find_element(*Locators.MAIN_SAUSE_PICKED).is_enabled()

    def test_main_filling_section_click_filling_shows(self, driver):

        driver.find_element(*Locators.MAIN_FILLING).click()

        assert driver.find_element(*Locators.MAIN_FILLING_PICKED).is_enabled()

    def test_main_bread_section_click_bread_shows(self, driver):

        driver.find_element(*Locators.MAIN_FILLING).click()
        driver.find_element(*Locators.MAIN_BREAD).click()

        assert driver.find_element(*Locators.MAIN_BREAD_PICKED).is_enabled()

