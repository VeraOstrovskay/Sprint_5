from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestTransit:

     # Тест перехода по клику на "Личный кабинет" с авторизованным пользователем
    def test_transition_to_account_page(self, driver_with_login):
       
        self.driver = driver_with_login
        self.driver.get(main_page)      
        
        
        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EXIT_BUTTON))
       

        assert self.driver.current_url == account_profile_url
        