from selenium.webdriver.common.by import By


class MainPageLocators:
    ELEMENTS_CARD = (By.XPATH, "//div[@class='category-cards']/div[1]")


class ElementsPageLocators:
    CHECKBOX_BUTTON = (By.ID, "item-1")


class CheckBoxPageLocators:
    HOME_TOGGLE = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    DOWNLOADS_TOGGLE = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
    WORD_FILE = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label')
    RESULT_TEXT = (By.ID, "result")
