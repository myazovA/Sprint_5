from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_personal_acc_click_page_open(main_personal_account, login_pass_recovery_btn, login_email, login_password,
                                      login_btn, main_logo, pers_acc_name):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))
    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, pers_acc_name)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.quit()


def test_personal_acc_construct_btn_click_main_page_open(main_personal_account, login_pass_recovery_btn, login_email,
                                                         login_password,login_btn, main_logo, pers_acc_name,
                                                         pers_acc_construct):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))
    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, pers_acc_name)))
    driver.find_element(By.XPATH, pers_acc_construct).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_personal_acc_logo_click_main_page_open(main_personal_account, login_pass_recovery_btn, login_email,
                                                         login_password,login_btn, main_logo, pers_acc_name,
                                                         pers_acc_logo):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))
    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, pers_acc_name)))
    driver.find_element(By.XPATH, pers_acc_logo).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_personal_acc_exit_login_page_open(main_personal_account, login_pass_recovery_btn, login_email,
                                                         login_password,login_btn, main_logo, pers_acc_name,
                                                         pers_acc_exit_btn):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_pass_recovery_btn)))

    driver.find_element(By.XPATH, login_email).send_keys('ArtemMyazov8000@yandex.ru')
    driver.find_element(By.XPATH, login_password).send_keys('123456')
    driver.find_element(By.XPATH, login_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, main_logo)))
    driver.find_element(By.XPATH, main_personal_account).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, pers_acc_name)))
    driver.find_element(By.XPATH, pers_acc_exit_btn).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, login_pass_recovery_btn)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()
