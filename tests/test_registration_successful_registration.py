import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.elements_to_find import TestLocators

#переменные
USER_NAME = 'P2er'
USER_EMAIL = 't23cpyt@mail.ru'
USER_PASSWORD = '12344232'

# Совершаем переход на старницу авторизации
def navigate_to_login_page(driver):
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
#Регистрация
def register_user(driver, user_name, user_email, user_password):
    driver.find_element(TestLocators.BUTTON_REGISTRATION).click()  # Кликаем кнопку Зарегистрироваться
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.INPUT_NAME)
    )
    driver.find_element(TestLocators.INPUT_NAME).send_keys(user_name)
    driver.find_element(TestLocators.INPUT_EMAIL).send_keys(
        user_email)
    driver.find_element(TestLocators.INPUT_PASSWORD).send_keys(user_password)
    driver.find_element(TestLocators.BUTTON_REGISTRATION_1).click()

#тест на удачную регистрацию
def login_user(driver, user_email, user_password):
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(user_email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(user_password)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))
    )
    text = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert text == 'Оформить заказ'

@pytest.mark.usefixtures("setup_driver")
def test_successful_registration(setup_driver):
    driver = setup_driver
    navigate_to_login_page(driver)
    register_user(driver, USER_NAME, USER_EMAIL, USER_PASSWORD)
    login_user(driver, USER_EMAIL, USER_PASSWORD)

if __name__ == "__main__":
    pytest.main()
