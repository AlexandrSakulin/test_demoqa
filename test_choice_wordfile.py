from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.checkbox_page import CheckBoxPage


def test_choice_worldfile_chrome(browser_chrome):
    """Проверяет возможность выбора WorldFile на браузере Chrome"""
    page_main = MainPage(browser_chrome)
    page_main.should_be_elements_card()
    page_main.go_to_elements_page()
    page_elements = ElementsPage(browser_chrome)
    page_elements.should_be_checkbox()
    page_elements.go_to_checkbox_page()
    page_checkbox = CheckBoxPage(browser_chrome)
    page_checkbox.should_be_toggle_home()
    page_checkbox.click_toggle_home()
    page_checkbox.click_toggle_downloads()
    page_checkbox.choise_worldfile()


def test_choice_worldfile_firefox(browser_firefox):
    """Проверяет возможность выбора WorldFile на браузере FireFox"""
    page_main = MainPage(browser_firefox)
    page_main.should_be_elements_card()
    page_main.go_to_elements_page()
    page_elements = ElementsPage(browser_firefox)
    page_elements.should_be_checkbox()
    page_elements.go_to_checkbox_page()
    page_checkbox = CheckBoxPage(browser_firefox)
    page_checkbox.should_be_toggle_home()
    page_checkbox.click_toggle_home()
    page_checkbox.click_toggle_downloads()
    page_checkbox.choise_worldfile()
