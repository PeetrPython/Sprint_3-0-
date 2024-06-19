import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

main_page = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def setup_driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(main_page)
    yield driver
    driver.quit()
