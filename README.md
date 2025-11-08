Sprint 5 
1. Создала файл curl.py c url адресами, используемыми в тестах

2. зарегистрировала пользователя данные содержатся в файле data.py

3. файл conftest.py содержит фикстуры 
    driver() - Фикстура для подключения вебдрайвера
    driver_with_login() - Фикстура для подключения вебдрайвера с входом в аккаунт и выходом из него

4. файл helper.py содержит генератор данных для проверки регистрации новых пользователей

5. файл locators.py содержит локаторы элементов страницы, используемые в тестах

6. файл tests/test_construction.py содержит тесты для раздела "Конструктор"
    TestCunstructorTransition - Класс с тестами элементов конструктора
        test_click_to_rolls_link_active() - проверка перехода при клике на раздел "Булки"
        test_click_to_sauses_link_active() - проверка перехода при клике на раздел "Соусы"
        test_click_to_toppings_link_active() - проверка перехода при клике на раздел "Начинки"

7. файл tests/test_login.py содержит тесты для входа
    TestLogin - Класс с тестами входа из разных мест
        _wait_and_fill_login_fields() - вспомогательный метод заподнения полей для авторизации пользователя
        test_from_login_button_success() - проверка входа по кнопке "Войти" на главной странице
        test_from_account_header_link_success() - проверка входа через кнопку "Личный кабинет"
        test_from_registration_form_link_success() - проверка входа через кнопку в форме регистрации
        test_from_forgot_password_form_link_success() - проверка входа через кнопку в форме восстановления пароля

8. файл tests/test_exit.py содержит тесты для выхода из аккаунта
    TestExitFromAccount - Класс с тестом выхода из аккаунта пользователя
        test_exit_from_main_page_login_page() - проверка выхода по кнопке "Выйти" в личном кабинете

9. файл tests/test_registration.py содержит тесты проверки регистрации пользователя
    TestRegistration - Класс с тестами формы регистрации
        _register_user() - вспомогательный метод заполнения полей для регистрации пользователя
        test_registration_generated_credentials_success() - проверка успешной регистрации при не пустом поле "Имя", email
            в формате логин@домен и пароле не меньше 6 символов
        test_registration_wrong_password_allert_shows() - проверка появления ошибки при пароле длиной меньше 6 символов
        test_registration_empty_name_page_not_changed() - проверка не успешной регистрации при пустом поле имя

10. файл tests/test_transit_by_click_to_personal_account.py содержит тест перехода в личный кабинет
    TestTransit - Класс с тестом перехода по клику на "Личный кабинет"
        test_transition_with_autorization_to_account_page() - проверка перехода по клику на "Личный кабинет" авторизованным  пользователем

11. файл tests/test_transit_from_accont.py содержит файлы с тестами перехода из личного кабинета
    TestTransitFromAccountProfile - Класс с тестами перехода из личного кабинета в конструктор
        test_by_click_to_contsructor_button_main_page() - проверка перехода по клику на кнопку "Конструктор"
        test_by_click_to_logo_main_page() - проверка перехода по клику на логотип Stellar Burgers.

