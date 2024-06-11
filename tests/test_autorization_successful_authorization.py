
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'te12s232tpyt@mail.ru'
PAS = '12344232'

# Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_main_button(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(EMAIL)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PAS)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))
    )
    text = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert text == 'Оформить заказ'

# Авторизация через Личный кабинет
def test_login_via_personal_cabinet(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 9).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(EMAIL)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PAS)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))
    )
    text = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert text == 'Оформить заказ'

# Вход через кнопку в форме восстановления пароля
def test_login_via_forgot_password_form(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click()  # Кликаем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(EMAIL)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PAS)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))
    )
    text = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert text == 'Оформить заказ'

if __name__ == "__main__":
    pytest.main()
