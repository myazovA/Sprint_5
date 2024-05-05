import pytest

#Страница Входа
@pytest.fixture(scope='session')
def login_registration():
    return './/p[1]/a' # Кнопка "Зарегестрироваться"

@pytest.fixture(scope='session')
def login_pass_recovery_btn():
    return './/p[2]/a[@class="Auth_link__1fOlj"]'  # Кнопка "Восстановить пароль"

@pytest.fixture(scope='session')
def login_email():
    return './/fieldset[1]/div/div/input' # Поле "Email"

@pytest.fixture(scope='session')
def login_password():
    return './/fieldset[2]/div/div/input' # Поле "Пароль"

@pytest.fixture(scope='session')
def login_btn():
    return './/form/button' # Кнопка "Войти"

@pytest.fixture(scope='session')
def login_reg_btn():
    return './/p[1]/a' # Кнопка "Зарегистрироваться"

#Главная страница
@pytest.fixture(scope='session')
def main_login_btn():
    return './/section[2]/div/button' # Кнопка "Войти в аккаунт" на главной

@pytest.fixture(scope='session')
def main_logo():
    return ".//div/a[@class='active']" # Логитип

@pytest.fixture(scope='session')
def main_personal_account():
    return ".//nav/a[@class='AppHeader_header__link__3D_hX']" # Кнопка "Личный кабинет"

@pytest.fixture(scope='session')
def main_bread():
    return './/section[1]/div[1]/div[1]' # Раздел "Булки"

@pytest.fixture(scope='session')
def main_r2_d2_bread():
    return '[alt="Флюоресцентная булка R2-D3"]' # Флюоресцентная булка R2-D3

@pytest.fixture(scope='session')
def main_sause():
    return './/section[1]/div[1]/div[2]' # Раздел "Соусы"

@pytest.fixture(scope='session')
def main_sause_galactic():
    return '[alt="Соус традиционный галактический"]' # "Соус традиционный галактический"

@pytest.fixture(scope='session')
def main_filling():
    return './/section[1]/div[1]/div[3]' # Раздел "Начинка"

@pytest.fixture(scope='session')
def main_filling_proto():
    return '[alt="Мясо бессмертных моллюсков Protostomia"]' # "Мясо бессмертных моллюсков Protostomia"

#Страница Регистрации
@pytest.fixture(scope='session')
def reg_name():
    return './/fieldset[1]/div/div/input' # Поле "Имя"

@pytest.fixture(scope='session')
def reg_email():
    return './/fieldset[2]/div/div/input' # Поле "Email"

@pytest.fixture(scope='session')
def reg_password():
    return './/fieldset[3]/div/div/input' # Поле "Пароль"

@pytest.fixture(scope='session')
def reg_reg_btn():
    return './/form/button' # Кнопка "Зарегестрироваться"

@pytest.fixture(scope='session')
def reg_pass_error():
    return ".//fieldset[3]/div/p[@class='input__error text_type_main-default']" # Надпись "Некорректный пароль"

@pytest.fixture(scope='session')
def reg_login_btn():
    return "//p/a[@class='Auth_link__1fOlj']" # Кнопка "Войти"

#Страница Восстановления пароля
@pytest.fixture(scope='session')
def pass_recovery_login():
    return "//p/a[@class='Auth_link__1fOlj']" # Кнопка "Войти"

#Страница Личный кабинет
@pytest.fixture(scope='session')
def pers_acc_name():
    return ".//li[1]/div/div/input" # Поле "Имя"

@pytest.fixture(scope='session')
def pers_acc_construct():
    return './/li[1]/a/p' # Кнопка "Конструктор"

@pytest.fixture(scope='session')
def pers_acc_logo():
    return './/nav/div/a' # Лого

@pytest.fixture(scope='session')
def pers_acc_exit_btn():
    return './/li[3]/button' # Кнопка выхода из аккаунта







