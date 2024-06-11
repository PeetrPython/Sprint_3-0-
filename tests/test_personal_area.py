import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'te12s232tpyt@mail.ru'
pas = '12344232'

def test_steps_personal_link(setup_driver):#Переход в личный кабинет
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pas)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']")))
    text1 = driver.find_element(By.XPATH,
                                ".//p[text()='В этом разделе вы можете изменить свои персональные данные']").text
    time.sleep(2)
    assert text1 == 'В этом разделе вы можете изменить свои персональные данные'

#Выход из аккаунта
def test_logout(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pas)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    text_out = driver.find_element(By.XPATH, ".//h2[text()='Вход']").text
    assert text_out == 'Вход'
    time.sleep(2)

if __name__ == "__main__":
    pytest.main()