from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint


def test_registration_correct_name_login_pass_successful_registration(login_registration, login_pass_recovery_btn,
                                                                      login_email, login_password, login_btn,
                                                                      main_login_btn, main_logo, reg_name, reg_email,
                                                                      reg_password, reg_reg_btn):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    num = randint(20, 999)
    email = f'ArtemMyazov8{num}@yandex.ru'

    driver.find_element(By.XPATH, main_login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))
    driver.find_element(By.XPATH, login_registration).click()

    driver.find_element(By.XPATH, reg_name).send_keys('Artem')
    driver.find_element(By.XPATH, reg_email).send_keys(email)
    driver.find_element(By.XPATH, reg_password).send_keys('123456')
    driver.find_element(By.XPATH, reg_reg_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys(email)
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_registration_correct_name_login_short_pass_unsuccessful_registration(login_registration, reg_reg_btn,
                                                                              login_pass_recovery_btn, main_login_btn,
                                                                              reg_name, reg_email, reg_password,
                                                                              reg_pass_error):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    num = randint(20, 999)
    email = f'ArtemMyazov8{num}@yandex.ru'

    driver.find_element(By.XPATH, main_login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))
    driver.find_element(By.XPATH, login_registration).click()

    driver.find_element(By.XPATH, reg_name).send_keys('Artem')
    driver.find_element(By.XPATH, reg_email).send_keys(email)
    driver.find_element(By.XPATH, reg_password).send_keys('12345')
    driver.find_element(By.XPATH, reg_reg_btn).click()

    assert expected_conditions.visibility_of_element_located((By.XPATH, reg_pass_error))



