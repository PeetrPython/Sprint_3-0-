import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators

email = 'te12s232tpyt@mail.ru'
pas = '12344232'

#Переход из личного кабинета в конструктор через stellaburger
def test_steps_logo_burger(setup_driver):#Переход в личный кабинет
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
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']")))
    driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()#клик по лого
    order_but = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    time.sleep(1)
    assert order_but.is_displayed()

#Переход из личного кабинета в конструктор
def test_steps_click_constructor(setup_driver):
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
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    order_but = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    time.sleep(1)
    assert order_but.is_displayed()

# Проверка конструктора, переключение на вкладку Соусы
def test_slide_constructor_sauces(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pas)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    time.sleep(1)
    sauces_tab = driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]")
    assert sauces_tab.is_displayed(), "Вкладка 'Соусы' является текущей активной вкладкой"
def test_slide_constructor_filling(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pas)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    time.sleep(1)
    sauces_tab = driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Начинки']]")
    assert sauces_tab.is_displayed(), "Вкладка 'Соусы' является текущей активной вкладкой"

def test_slide_constructor_bread(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pas)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    time.sleep(1)
    sauces_tab = driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]")
    assert sauces_tab.is_displayed(), "Вкладка 'Соусы' является текущей активной вкладкой"


if __name__ == "__main__":
    pytest.main()