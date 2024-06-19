from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_TO_ACCOUUNT = By.XPATH, ".//button[text()='Войти в аккаунт']"
    LOGIN = By.XPATH, ".//h2[text()='Вход']"
    LOGIN_TO_ACCOUUNT_REG = By.XPATH, ".//button[text()='Войти']"
    BUTTON_REGISTRATION = By.XPATH, ".//a[@class='Auth_link__1fOlj']"
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']"
    INPUT_PASSWORD = By.XPATH, ".//input[@type='password']"
    BUTTON_REGISTRATION_1 = By.XPATH, ".//button[text()='Зарегистрироваться']"
    PERSONAL_AREA = By.XPATH, ".//p[text()='Личный Кабинет']"
