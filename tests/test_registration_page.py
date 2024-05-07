from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from locators import Locators
from data import PASSWORD, NAME, URL_MAIN_PAGE, SHORT_PASSWORD

class TestRegistrationPage:

    def test_registration_correct_name_login_pass_successful_registration(self, driver):

        num = randint(20, 999)
        email = f'ArtemMyazov8{num}@yandex.ru'

        driver.find_element(*Locators.MAIN_LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))
        driver.find_element(*Locators.LOGIN_REGISTRATION).click()

        driver.find_element(*Locators.REG_NAME).send_keys(NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.REG_REG_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_registration_correct_name_login_short_pass_unsuccessful_registration(self, driver):

        num = randint(20, 999)
        email = f'ArtemMyazov8{num}@yandex.ru'

        driver.find_element(*Locators.MAIN_LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))
        driver.find_element(*Locators.LOGIN_REGISTRATION).click()

        driver.find_element(*Locators.REG_NAME).send_keys(NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(SHORT_PASSWORD)
        driver.find_element(*Locators.REG_REG_BTN).click()

        assert expected_conditions.visibility_of_element_located((Locators.REG_PASS_ERROR))
