from .base_page import BasePage
from .locators import CheckBoxPageLocators


class CheckBoxPage(BasePage, CheckBoxPageLocators):
    def click_toggle_home(self):
        """Нажимаем на переключатель Home"""
        self.find_element(*self.HOME_TOGGLE).click()
        assert self.is_element_present(self.DOWNLOADS_TOGGLE), "Подменю home не раскрылось"

    def click_toggle_downloads(self):
        """Нажимаем на переключатель Downloads"""
        self.find_element(*self.DOWNLOADS_TOGGLE).click()
        assert self.is_element_present(self.WORD_FILE), "Подменю downloads не раскрылось"

    def choise_worldfile(self):
        """Выбираем World File"""
        self.find_element(*self.WORD_FILE).click()
        text_element = self.is_element_present(self.RESULT_TEXT).text
        assert text_element == 'You have selected :\nwordFile', "Сообщение 'You have selected: wordFile' отсутствует"
