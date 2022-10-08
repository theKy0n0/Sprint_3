# Файл с локаторами

class MainPage: #Локаторы для главной страницы
    LOGIN_BUTTON = '//*[@id="root"]/div/main/section[2]/div/button'  # Кнопка "Войти в аккаунт"
    PERSONAL_CABINET = '#root > div > header > nav > a > p'  # Личный кабинет
    WELCOME_TITLE = './/h1[contains(text(), "Собери")]'  # Текст "Соберите бургер"
    LOGO = 'div > a > svg'  # Логотип

class ConstructorPage: # Локаторы для страницы конструктора
    BULKA_SECTION_TAB = './/span[contains(text(), "Булки")]'  # Вкладка с булками
    BULKA_SECTION = './/h2[contains(text(), "улки")]'  # Секция "Булки"
    BULKA_ELEMENTS = './/p[contains(text(), "булка")]'  # Элементы в секции "Булки"
    SOUSI_SECTION_TAB = './/span[contains(text(), "Соусы")]'  # Вкладка с соусами
    SOUSI_SECTION = './/h2[contains(text(), "оус")]'  # Секция "Соусы"
    SOUSI_ELEMENTS = './/p[contains(text(), "оус")]'  # Элементы в секции "Соусы"
    NACHINKA_SECTION_TAB = './/span[contains(text(), "Начинки")]'  # Вкладка с начинками
    NACHINKA_SECTION = './/h2[contains(text(), "ачинк")]'  # Секция "Начинки"
    NACHINKA_FIRST = '[alt~=метеорит]'  # Первый элемент во вкладке с начинками
    NACHINKA_LAST = '[alt~=Сыр]'  # Последний элемент во вкладке с начинками

class AuthPage: # Локаторы для страницы авторизации
    EMAIL_FIELD = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Email"
    PASS_FIELD = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Пароль"
    LOGIN_BUTTON = '#root > div > main > div > form > button'  # Кнопка "Войти"
    REG_NEW_USER_BUTTON = 'a[href*="/register"]'  # Кнопка "Зарегистрироваться"
    PERSONAL_CABINET = '#root > div > header > nav > a > p'  # Кнопка "Личный кабинет" для страницы "Авторизация"

class RegPage: # Локаторы для страницы регистрации
    NAME_FIELD = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Имя"
    EMAIL_FIELD = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Email"
    PASS_FIELD = '[type="password"]'  # Поле "Пароль"
    REG_BUTTON = './/button[contains(text(), "ться")]'  # Кнопка "Зарегистрироваться"
    REG_ERROR_POPUP = '[class="input__error text_type_main-default"]'  # Поп-ап ошибки
    REG_ENTER_BUTTON = '//*[@id="root"]/div/main/div/div/p/a' # Кнопка "Войти" на странице регистрации

class PersonalCabinet: # локаторы для страницы личного кабинета
    NAME_FIELD = '/html/body/div/div/main/div/div/div/ul/li[1]/div/div/input[@value="Четкий Котангенс"]'  # Поле "Имя"
    LOGIN_FIELD = '/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input[@value="sergey_moskovskiy_03_030@ya.ru"]' # Поле "Логин", нужно обновлять на соответствующий логин из словаря cred_data при изменении
    PASS_FIELD = '//*[@id="root"]/div/main/div/div/div/ul/li[3]/div/div/input[@value="*****"]' # Поле "Пароль"
    ORDER_HISTORY_BUTTON = 'a[href*="order-history"]'  # Кнопка "История заказов"
    LOGOUT_BUTTON = './/button[contains(text(), "Выход")]'  # Кнопка "Выход"
    CONSTRUCTOR_BUTTON = '//*[@id="root"]/div/header/nav/ul/li[1]/a/p' # Кнопка "Конутруктор"

class RecoveryPage: # Локаторы для страницы востановления пароля
    RECOVERY_ENTER_BUTTON = '//*[@id="root"]/div/main/div/div/p/a' # Кнопка "Войти" на странице востановления пароля