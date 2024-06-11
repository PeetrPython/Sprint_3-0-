import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#переменные
USER_NAME = 'Per'
USER_EMAIL = 't2s232tpyt@mail.ru'
PASSWORD = '123456'
INVALID_PASSWORD = '12345'

# Регистрация с некорректным паролем
def test_register_user_invalid_pas(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click()
    driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']").send_keys(USER_NAME)
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']").send_keys(USER_EMAIL)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(INVALID_PASSWORD)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
    err_pas = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").text
    assert err_pas == 'Некорректный пароль'

#Регистрация с незаполненым именем
def test_register_invalid_name(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click()
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']").send_keys(USER_EMAIL)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until_not(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

def test_register_invalid_email(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
    )
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
    )
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click()
    driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']").send_keys(USER_NAME)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until_not(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))


if __name__ == "__main__":
    pytest.main()
