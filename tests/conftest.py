import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope='function') # scope=fixture посмотреть
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
