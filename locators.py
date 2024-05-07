from selenium.webdriver.common.by import By

class Locators:

    # Страница Входа
    LOGIN_REGISTRATION = (By.XPATH, './/p/a[@href="/register"]')  # Кнопка "Зарегестрироваться"
    LOGIN_PASS_RECOVERY_BTN =(By.XPATH , './/p/a[@href="/forgot-password"]')  # Кнопка "Восстановить пароль"
    LOGIN_EMAIL = (By.XPATH, './/fieldset/div/div[contains(@class,"type_text")]/input[@type="text"]') # Поле "Email"
    LOGIN_PASSWORD = (By.XPATH, './/fieldset/div/div[contains(@class,"type_password")]/input[@type="password"]') # Поле "Пароль"
    LOGIN_BTN = (By.XPATH, './/form/button[contains(@class, "button_type")]') # Кнопка "Войти"

    # Главная страница
    MAIN_LOGIN_BTN = (By.XPATH , './/section/div/button[contains(@class, "button_type")]')  # Кнопка "Войти в аккаунт"
    MAIN_LOGO = (By.XPATH, ".//div/a[@class='active']") # Логитип
    MAIN_PERSONAL_ACCOUNT = (By.XPATH, ".//nav/a[@class='AppHeader_header__link__3D_hX']") # Кнопка "Личный кабинет"
    MAIN_BREAD = (By.XPATH, ".//section/div/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']") # Раздел "Булки"
    MAIN_BREAD_PICKED = (By.XPATH, ".//section/div/div[contains(@class, 'tab_tab_type_current')]/span[text()='Булки']") # Флюоресцентная булка R2-D3
    MAIN_SAUSE = (By.XPATH, ".//section/div/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']") # Раздел "Соусы"
    MAIN_SAUSE_PICKED = (By.XPATH, ".//section/div/div[contains(@class, 'tab_tab_type_current')]/span[text()='Соусы']") # "Соус традиционный галактический"
    MAIN_FILLING = (By.XPATH, ".//section/div/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']") # Раздел "Начинка"
    MAIN_FILLING_PICKED = (By.XPATH, ".//section/div/div[contains(@class, 'tab_tab_type_current')]/span[text()='Начинки']") # "Мясо бессмертных моллюсков Protostomia"

    # Страница Регистрации
    REG_NAME = (By.XPATH, './/fieldset[1]/div/div/input') # Поле "Имя"
    REG_EMAIL = (By.XPATH, './/fieldset[2]/div/div/input') # Поле "Email"
    REG_PASSWORD = (By.XPATH, './/fieldset/div/div[contains(@class, "type_password")]/input[@type="password"]') # Поле "Пароль"
    REG_REG_BTN = (By.XPATH, './/form/button[contains(@class, "button_type")]') # Кнопка "Зарегестрироваться"
    REG_PASS_ERROR = (By.XPATH, ".//fieldset/div/p[@class='input__error text_type_main-default']") # Надпись "Некорректный пароль"
    REG_LOGIN = (By.XPATH, "//p/a[@class='Auth_link__1fOlj']") # Кнопка "Войти"

    # Страница Восстановления пароля
    PASS_RECOVERY_LOGIN = (By.XPATH, "//p/a[@class='Auth_link__1fOlj']") # Кнопка "Войти"

    # Страница Личный кабинет
    PERS_ACC_NAME = (By.XPATH, ".//li/div/div/input[@name='Name']") # Поле "Имя"
    PERS_ACC_CONSTRUCT = (By.XPATH, './/li/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]') # Кнопка "Конструктор"
    PERS_ACC_LOGO = (By.XPATH, './/nav/div/a[@href="/"]') # Лого
    PERS_ACC_EXIT_BTN = (By.XPATH, './/li/button[contains(@class, "text_type")]') # Кнопка выхода из аккаунта


