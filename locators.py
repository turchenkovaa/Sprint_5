from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главная страница"""
    main_form = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # Форма главной страницы сайта
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    login_account_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка войти в аккаунт
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    bun_btn = (By.XPATH, ".//span[text() = 'Булки']")  # Кнопка переключения на булки
    sauces_btn = (By.XPATH, ".//span[text() = 'Соусы']")  # Кнопка переключения на соусы
    toppings_btn = (By.XPATH, ".//span[text() = 'Начинки']")  # Кнопка переключения на начинки
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']")  # Текст соусы на главной странице
    sauces_ul = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Выбор соусов на главной странице
    bun = (By.XPATH, ".//h2[text() = 'Булки']")  # Текст булки на главной странице
    bun_ul = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Выбор булок на главной странице
    topping = (By.XPATH, ".//h2[text() = 'Начинки']")  # Текст начинки на главной странице
    topping_ul = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Выбор начинок на главной странице


class AuthPageLocators:
    """Форма авторизации"""
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка войти
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка восстановить пароль
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета


class RegistrationPageLocators:
    """Форма регистрации"""
    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    registration_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    error_message_double_reg = (
    By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации
    error_message_incorrect_password = (
    By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class RecoverPageLocators:
    """Форма восстановления пароля"""
    email_input = (By.XPATH, ".//label[text() = 'Email']")  # Поле ввода email
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка восстановить
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета


class PersonalAreaLocators:
    """Форма личного кабинета"""
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиль
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка история заказов
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    cansel_btn = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмена
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета