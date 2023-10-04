from .base_page import BasePage
from .locators import CheckBoxPageLocators


class CheckBoxPage(BasePage, CheckBoxPageLocators):
    def should_be_toggle_home(self):
        """Проверяет наличие переключателя"""
        assert self.is_element_present(self.HOME_TOGGLE), "Переключатель Home отсутствует"

    def click_toggle_home(self):
        """Нажимаем на переключатель Home"""
        (self.driver.find_element(*self.HOME_TOGGLE)).click()
        assert self.is_element_present(self.DOWNLOADS_TOGGLE), "Подменю home не раскрылось"

    def click_toggle_downloads(self):
        """Нажимаем на переключатель Downloads"""
        (self.driver.find_element(*self.DOWNLOADS_TOGGLE)).click()
        assert self.is_element_present(self.WORD_FILE), "Подменю downloads не раскрылось"

    def choise_worldfile(self):
        """Выбираем World File"""
        (self.driver.find_element(*self.WORD_FILE)).click()
        assert self.is_element_present(self.RESULT_TEXT), "Сообщение 'You have selected: wordFile' отсутствует"

