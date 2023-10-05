import pytest
from selenium import webdriver

from configurations import MAIN_URL


def get_firefox():
    return webdriver.Firefox()


def get_chrome():
    return webdriver.Chrome()


BROWSER_TYPE = {"chrome": get_chrome, "firefox": get_firefox}


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
    driver = BROWSER_TYPE[browser_type]()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
