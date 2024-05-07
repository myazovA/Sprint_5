from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import EMAIL, PASSWORD, URL_MAIN_PAGE

class TestLoginPage:

    def test_login_from_main_page_correct_login_pass_successful_login(self, driver):

        driver.find_element(*Locators.MAIN_LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_login_from_personal_acc_correct_login_pass_successful_login(self, driver):

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_login_from_reg_form_correct_login_pass_successful_login(self, driver):

        driver.find_element(*Locators.MAIN_LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))
        driver.find_element(*Locators.LOGIN_REGISTRATION).click()
        driver.find_element(*Locators.REG_LOGIN).click()

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_login_from_pass_recovery_correct_login_pass_successful_login(self, driver):

        driver.find_element(*Locators.MAIN_LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))
        driver.find_element(*Locators.LOGIN_PASS_RECOVERY_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.PASS_RECOVERY_LOGIN)))
        driver.find_element(*Locators.PASS_RECOVERY_LOGIN).click()

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE


