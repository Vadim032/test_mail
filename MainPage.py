from BaseApp import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[@class='ph-login svelte-1hiqrvn']")


class MainPage(BasePage):
    def click_login_button(self):
        login_button = self.find_element(MainPageLocators.LOCATOR_LOGIN_BUTTON)
        login_button.click()