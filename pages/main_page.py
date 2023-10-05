from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    def go_to_elements_page(self):
        """Осуществляет переход на страницу Elements"""
        self.find_element(*self.ELEMENTS_CARD).click()
        assert "elements" in self.driver.current_url.lower(), "При нажатии карточку Elements переход не произошел"
