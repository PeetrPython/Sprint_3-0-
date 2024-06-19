import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators

#переменные
USER_NAME = 'R2D2'
USER_EMAIL = 'c3pos@mail.ru'
USER_PASSWORD = '123456'

# Совершаем переход на старницу авторизации
def test_navigate_to_login_page(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    login = driver.find_element(*TestLocators.LOGIN)
    assert login.is_displayed()

#тест на удачную регистрацию
def test_register_user(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()  # Кликаем кнопку Зарегистрироваться
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.INPUT_NAME)
    )
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(
        USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_1).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    login_but = driver.find_element(*TestLocators.LOGIN)
    assert login_but.is_displayed()

#вход через кнопку в форме регистрации
def test_login_user(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    login = driver.find_element(*TestLocators.LOGIN)
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))
    )
    order_button = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    assert order_button.is_displayed()

if __name__ == "__main__":
    pytest.main()
