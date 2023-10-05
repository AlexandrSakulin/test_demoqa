from .base_page import BasePage
from .locators import ElementsPageLocators


class ElementsPage(BasePage, ElementsPageLocators):
    def go_to_checkbox_page(self):
        """В раскрытом меню кликаем Check Box"""
        self.find_element(*self.CHECKBOX_BUTTON).click()
        assert "checkbox" in self.driver.current_url.lower(), "При нажатии на кнопку 'Check box' переход не произошел"
