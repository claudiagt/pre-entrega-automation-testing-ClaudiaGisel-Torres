import pytest
from utils.driver_factory import get_driver
from utils.actions import Actions
from utils.locators import LoginPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    actions = Actions(driver)

    # Abrimos la página
    driver.get("https://www.saucedemo.com/")

    # Hacemos login
    actions.type(LoginPage.USERNAME, "standard_user")
    actions.type(LoginPage.PASSWORD, "secret_sauce")
    actions.click(LoginPage.LOGIN_BTN)

    return driver