from .base_page import BasePage
from .locators import ElementsPageLocators


class ElementsPage(BasePage, ElementsPageLocators):
    def should_be_checkbox(self):
        """Проверяет наличие Checkbox"""
        assert self.is_element_present(self.CHECKBOX_BUTTON), "Сheckbox отсутствует"

    def go_to_checkbox_page(self):
        """В раскрытом меню кликаем Check Box"""
        (self.driver.find_element(*self.CHECKBOX_BUTTON)).click()
        assert "checkbox" in self.driver.current_url.lower(), "При нажатии переход не произошел"
