import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def setup_driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
# def navigate_to_login_page(): # Совершаем переход на старницу авторизации
#     WebDriverWait(driver, 3).until(
#         EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']"))
#     )
#     driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
#     WebDriverWait(driver, 3).until(
#         EC.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))
#     )