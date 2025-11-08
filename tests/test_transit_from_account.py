from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestTransitFromAccount:

    # Тест перехода из личного кабинета по клику на "Конструктор"
    def test_by_click_to_contsructor_button_main_page(self, driver_with_login):
        
        self.driver = driver_with_login

        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EXIT_BUTTON))

        
        self.driver.find_element(*Locators.CONSTRUCT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK))

        
        assert self.driver.find_element(*Locators.ACTIVE_HEADER_LINK).text == 'Конструктор'
        assert self.driver.current_url == main_page

    # Тест перехода из личного кабинета по клику на логотип
    def test_by_click_to_logo_main_page(self, driver_with_login):
        
        self.driver = driver_with_login

        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EXIT_BUTTON))
        
        
        self.driver.find_element(*Locators.LOGO_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK))

        
        assert self.driver.current_url == main_page
        
        