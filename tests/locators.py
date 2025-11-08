from selenium.webdriver.common.by import By

class Locators:

    # Локаторы для страницы регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    REG_ERROR       = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    REG_NAME            = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")
    REG_EMAIL           = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    REG_PASSWORD        = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
 

    # Локаторы для главной страницы
    ACCOUNT_LOGIN_BUTTON    = (By.XPATH, "//main//button[contains(text(), 'Войти в аккаунт')]")
    BURGER_CONSTRUCTOR_BUTTON = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]//button")
    MAKE_ORDER_BUTTON       = (By.XPATH, "//main//button[contains(text(), 'Оформить заказ')]")
    ACCOUNT_HEADER_LINK     = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")
    LOGO_HEADER_LINK        = (By.XPATH, "//header/nav/div[contains(@class,'logo')]")
    CONSTRUCT_HEADER_LINK   = (By.XPATH, "//header/nav//a//p[contains(text(), 'Конструктор')]")
    ACTIVE_HEADER_LINK      = (By.XPATH, "//header//nav//a[contains(@class,'link_active')]")

    CONSTRUCT_ROLLS_LINK    = (By.XPATH, "//main//div[span[contains(text(), 'Булки')]]")
    CONSTRUCT_ROLLS_HEADER = (By.XPATH, "//h2[contains(text(),'Булки')]")
    CONSTRUCT_SAUCES_LINK   = (By.XPATH, "//main//div[span[contains(text(), 'Соусы')]]")
    CONSTRUCT_SAUCES_HEADER = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    CONSTRUCT_TOPPINGS_LINK = (By.XPATH, "//main//div[span[contains(text(), 'Начинки')]]")
    CONSTRUCT_TOPPINGS_HEADER = (By.XPATH, "//h2[contains(text(),'Начинки')]")    
    CONSTRUCT_LINK_ACTIVE   = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Дополнительные локаторы для теста входа в личный кабинет
    REGISTER_LOGIN_LINK        = (By.XPATH, "//main//a[@href = '/login']")
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, "//main//a[@href = '/login']")

    LOGIN_EMAIL = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    LOGIN_PASSWORD = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, 'Auth_form')]//button[contains(text(), 'Войти')]")
    
    
    # Локаторы для теста выхода из личного кабинета
    ACCOUNT_EXIT_BUTTON  = (By.XPATH, "//nav//button[contains(text(), 'Выход')]")

    # Локаторы ошибок:
    ERROR_PASSWORD_TEXT = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

