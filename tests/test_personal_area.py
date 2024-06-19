import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators

email = 'te12s232tpyt@mail.ru'
pas = '12344232'

def test_steps_personal_link(setup_driver):#Переход в личный кабинет
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(pas)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']")))
    personal_area = driver.find_element(By.XPATH,
                                ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")
    time.sleep(2)
    assert personal_area.is_displayed()

#Выход из аккаунта
def test_logout(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(pas)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    button_registration = driver.find_element(By.XPATH, ".//h2[text()='Вход']")
    assert button_registration.is_displayed()
    time.sleep(2)

if __name__ == "__main__":
    pytest.main()