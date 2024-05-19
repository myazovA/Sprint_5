import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.get('https://stellarburgers.nomoreparties.site/')

    yield chrome

    chrome.quit()