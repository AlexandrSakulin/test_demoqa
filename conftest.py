import pytest
from selenium import webdriver
from configurations import MAIN_URL


BROWSER_TYPE = {"chrome": "chromedriver", "firefox": "geckodriver"}


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбери браузер, есть chrome и firefox, по умолчанию: %(default)",
    )


@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser")
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
