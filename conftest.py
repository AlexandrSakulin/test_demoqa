import pytest
from selenium import webdriver
from configurations import MAIN_URL

@pytest.fixture
def browser_chrome(request):
    """Автоматически открывает указанный URL-адрес MAIN_URL перед началом теста и
    закрывает браузер после завершения теста"""
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
def browser_firefox(request):
    """Автоматически открывает указанный URL-адрес MAIN_URL перед началом теста и
    закрывает браузер после завершения теста"""
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()