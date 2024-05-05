from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

def test_main_sause_section_click_sause_shows(main_sause, main_sause_galactic):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_sause).click()

    assert driver.find_element(By.CSS_SELECTOR, main_sause_galactic).is_displayed()
    driver.quit()

def test_main_filling_section_click_filling_shows(main_filling, main_filling_proto):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_filling).click()

    assert driver.find_element(By.CSS_SELECTOR, main_filling_proto).is_displayed()
    driver.quit()

def test_main_bread_section_click_bread_shows(main_bread, main_filling, main_r2_d2_bread):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, main_filling).click()
    driver.find_element(By.XPATH, main_bread).click()

    assert driver.find_element(By.CSS_SELECTOR, main_r2_d2_bread).is_displayed()
    driver.quit()
