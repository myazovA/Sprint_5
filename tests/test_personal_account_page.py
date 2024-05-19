from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import URL_MAIN_PAGE, EMAIL, PASSWORD, URL_PERS_ACC_PAGE, URL_LOGIN_PAGE

class TestPersonalAccountPage:

    def test_personal_acc_click_page_open(self, driver):

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.PERS_ACC_NAME)))

        assert driver.current_url == URL_PERS_ACC_PAGE

    def test_personal_acc_construct_btn_click_main_page_open(self, driver):

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.PERS_ACC_NAME)))

        driver.find_element(*Locators.PERS_ACC_CONSTRUCT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_personal_acc_logo_click_main_page_open(self, driver):

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.PERS_ACC_NAME)))

        driver.find_element(*Locators.PERS_ACC_LOGO).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        assert driver.current_url == URL_MAIN_PAGE

    def test_personal_acc_exit_login_page_open(self, driver):

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.MAIN_LOGO)))

        driver.find_element(*Locators.MAIN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.PERS_ACC_NAME)))

        driver.find_element(*Locators.PERS_ACC_EXIT_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.LOGIN_PASS_RECOVERY_BTN)))

        assert driver.current_url == URL_LOGIN_PAGE

