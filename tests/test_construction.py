import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestCunstructorTransition:

    # Тестирование перехода по клику на Соусы и Начинки
    @pytest.mark.parametrize("tab_text, tab_link, header_text", [
        (ConstructorTabText.sauces, Locators.CONSTRUCT_SAUCES_LINK, Locators.CONSTRUCT_SAUCES_HEADER),  # Проверка при клике на соусы
        (ConstructorTabText.toppings, Locators.CONSTRUCT_TOPPINGS_LINK, Locators.CONSTRUCT_TOPPINGS_HEADER),  # Проверка при клике на Начинки
    ])
    def test_click_to_sauses_link_active(self, driver_with_login, tab_text, tab_link, header_text):
        self.driver = driver_with_login

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(tab_link)).click()
        scrolled_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(header_text))

        assert scrolled_element.is_displayed()
        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == tab_text

    # Тестирование перехода по кику на Булки - Требуется дополнительное действие по переходу
    def test_click_to_rolls_link_active(self, driver_with_login):
        self.driver = driver_with_login
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_TOPPINGS_LINK)).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK)).click()

        scrolled_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_HEADER))
        assert scrolled_element.is_displayed()

        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == 'Булки'
        
        