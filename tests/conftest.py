import pytest
from selenium import webdriver
from locators import TestLocators
from data import UsersTestData


# Фикстура WebDriver
@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


# Фикстура для авторизации с валидной парой логин и пароль перед тестами
@pytest.fixture
def login(driver):
    driver.find_element(*TestLocators.button_login_in_main).click()
    driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
    driver.find_element(*TestLocators.button_login).click()

    