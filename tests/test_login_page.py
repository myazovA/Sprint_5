from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_login_from_main_page_correct_login_pass_successful_login(main_login_btn, login_pass_recovery_btn, login_email,
                                                                  login_password, login_btn, main_logo):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_login_from_personal_acc_correct_login_pass_successful_login(main_personal_account, login_pass_recovery_btn,
                                                                     login_email,login_password, login_btn, main_logo):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_login_from_reg_form_correct_login_pass_successful_login(main_login_btn, login_email,login_password,
                                                                 login_btn, main_logo, login_pass_recovery_btn,
                                                                 login_reg_btn, reg_login_btn):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))
    driver.find_element(By.XPATH, login_reg_btn).click()
    driver.find_element(By.XPATH, reg_login_btn).click()

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_login_from_pass_recovery_correct_login_pass_successful_login(main_login_btn, login_email, login_password,
                                                                      login_btn, main_logo, login_pass_recovery_btn,
                                                                      pass_recovery_login):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_login_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))
    driver.find_element(By.XPATH, login_pass_recovery_btn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, pass_recovery_login)))
    driver.find_element(By.XPATH, pass_recovery_login).click()

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

