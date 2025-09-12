
from selenium.webdriver.common.by import By


class TestLocators:
    # РЕГИСТРАЦИЯ
    # Поле Имя
    input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    # Поле Email
    input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'

    # Поле Пароль
    input_password = By.XPATH, './/input[@name="Пароль"]'

    # Кнопка Зарегистрироваться
    button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    # Сообщение об ошибке: Некорректный ппароль
    notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Кнопка Войти при регистрации
    button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

    # АУТЕНТИФИКАЦИЯ
    # Поле Email
    input_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # Поле Пароль
    input_password_auth = By.XPATH, '//input[@name = "Пароль"]'

    # Кнопка Войти
    button_login = By.XPATH, '//button[text()="Войти"]'

    # Кнопка Зарегистрироваться
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Кнопка Восстановить пароль
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка Войти при восстановления пароля
    button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]'

    # ЛИЧНЫЙ КАБИНЕТ
    # Профиль
    profile = By.XPATH, '//a[@href = "/account/profile"]'

    # История заказов
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка Выйти
    button_logout = By.XPATH, '//button[@type = "button"]'

    # ГЛАВНАЯ СТРАНИЦА
    # Кнопка "Войти в аккаунт"
    button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # Кнопка "Личный кабинет"
    button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Оформить заказ"
    button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Конструктор"
    header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]'

    # Селектор, помечающий выбранный раздел конструктора как активный
    selected_button = By.XPATH, ('//div[@class = '
                                 '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')

    # Заголовок раздела "Булки" в меню 
    buns_block = By.XPATH, '//span[text() = "Булки"]'

    # Заголовок раздела "Соусы" в меню 
    sauces_block = By.XPATH, '//span[text() = "Соусы"]'

    # Заголовок раздела "Начинки" в меню
    fillings_block = By.XPATH, '//span[text() = "Начинки"]'

    # Кликабельный логотип в шапке сайта
    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'
