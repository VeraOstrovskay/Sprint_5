from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistration:     
        
        
        
    # Успешная регистрация с сгенерированными данными
    def test_registration_generated_credentials_success(self, driver):
        self.driver = driver
        name, email, password = generate_registration_data()

        self.driver.get(registration_url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_BUTTON))
        self.driver.find_element(*Locators.REG_NAME).send_keys(name)
        self.driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(self.driver.current_url))
        assert self.driver.current_url == account_login

    # Появление ошибки при длине пароля меньше 6 символов
    def test_registration_wrong_password_allert_shows(self, driver):
        
        self.driver = driver   
        name, email, password = generate_registration_data()
        password = '123'
        
       
        self.driver.get(registration_url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_BUTTON))
        self.driver.find_element(*Locators.REG_NAME).send_keys(name)
        self.driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        error_text_element = self.driver.find_element(*Locators.ERROR_PASSWORD_TEXT)
        assert error_text_element.is_displayed()  == True

    # Не успешная регистрация при пустом поле имя
    def test_registration_empty_name_page_not_changed(self, driver):
       
        self.driver = driver
        name, email, password = generate_registration_data()
        name = ''

       
        self.driver.get(registration_url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_BUTTON))

        self.driver.find_element(*Locators.REG_NAME).send_keys(name)
        self.driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        assert self.driver.current_url  == registration_url

        

