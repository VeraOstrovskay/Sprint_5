from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestLogin:
    
    # Вспомогательный метод для заполнения полей при авторизации
    def _wait_and_fill_login_fields(self):

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        
        self.driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        self.driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        
    # Тестирование входа по кнопке "Войти в аккаунт" на главной странице
    def test_from_login_button_success(self, driver):
        
        self.driver = driver
        self.driver.get(main_page)

        # задаем явное ожидание загрузки страницы входа
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_LOGIN_BUTTON))
        
        self.driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()

        self._wait_and_fill_login_fields()
        
        main_button_text = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
        
        assert main_button_text == 'Оформить заказ'
        assert self.driver.current_url == main_page

    # Тестирование входа через кнопку "Личный Кабинет"
    def test_from_account_header_link_main_success(self, driver):
       
        self.driver = driver
        self.driver.get(main_page)

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))
        
        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()

        self._wait_and_fill_login_fields()

        main_button_text = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
       

        assert main_button_text == 'Оформить заказ'
        assert self.driver.current_url == main_page

    # Тестирование входа через кнопку в форме регистрации
    def test_from_registration_form_link_success(self, driver):
        
        self.driver = driver
        self.driver.get(registration_url)

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_LOGIN_LINK))
     
        self.driver.find_element(*Locators.REGISTER_LOGIN_LINK).click()

        self._wait_and_fill_login_fields()

        main_button_text = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
      

        assert main_button_text == 'Оформить заказ'
        assert self.driver.current_url == main_page

    # Тестирование входа через кнопку в форме восстановления пароля
    def test_from_forgot_password_form_link_success(self, driver):
       
        self.driver = driver
        self.driver.get(forgot_password_url)

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FORGOT_PASSWORD_LOGIN_LINK))
        self.driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN_LINK).click()

        self._wait_and_fill_login_fields()

        main_button_text = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
      

        assert main_button_text == 'Оформить заказ'
        assert self.driver.current_url == main_page

