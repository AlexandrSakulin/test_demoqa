from selenium.webdriver.common.by import By


class MainPageLocators:
    ELEMENTS_CARD = (By.XPATH, "//div[@class='category-cards']/div[1]")


class ElementsPageLocators:
    CHECKBOX_BUTTON = (By.ID, "item-1")


class CheckBoxPageLocators:
    HOME_TOGGLE = (By.XPATH, "//span[text()='Home']/../../button[@title='Toggle']")
    DOWNLOADS_TOGGLE = (By.XPATH, "//span[text()='Downloads']/../../button[@title='Toggle']")
    WORD_FILE = (By.XPATH, "//span[text()='Word File.doc']")
    RESULT_TEXT = (By.ID, "result")
