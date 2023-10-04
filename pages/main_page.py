from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    def should_be_elements_card(self):
        """Проверяет наличие Elements"""
        assert self.is_element_present(self.ELEMENTS_CARD), "Elements отсутствует"

    def go_to_elements_page(self):
        """Осуществляет переход на страницу Elements"""
        (self.driver.find_element(*self.ELEMENTS_CARD)).click()
        assert "elements" in self.driver.current_url.lower(), "При нажатии переход не произошел"
