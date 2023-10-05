import allure

from pages.checkbox_page import CheckBoxPage
from pages.elements_page import ElementsPage
from pages.main_page import MainPage


@allure.title("Проверка возможности выбора WorldFile")
def test_choice_worldfile(browser):

    with allure.step("Переход на страницу элементов"):
        page_main = MainPage(browser)
        page_main.go_to_elements_page()

    with allure.step("Переход на страницу Elements"):
        page_elements = ElementsPage(browser)
        page_elements.go_to_checkbox_page()

    with allure.step("Переход на страницу checkbox"):
        page_checkbox = CheckBoxPage(browser)
        page_checkbox.click_toggle_home()
        page_checkbox.click_toggle_downloads()

    with allure.step("Выбор файла Word file.doc"):
        page_checkbox.choise_worldfile()
