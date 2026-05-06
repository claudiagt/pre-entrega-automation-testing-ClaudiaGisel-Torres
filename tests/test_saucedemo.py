
from utils.actions import Actions
from utils.locators import LoginPage
from utils.locators import InventoryPage
from utils.locators import LoginPage, InventoryPage
from utils.locators import LoginPage, InventoryPage, CartPage


#test login

def test_abrir_pagina(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title


def test_login_success(login):
    driver = login

    # Validamos que cambió la URL
    assert "inventory.html" in driver.current_url

#Test inventario productos

def test_inventory_page(login):
    driver = login
    actions = Actions(driver)

    # 1. Validar título
    title = actions.get_text(InventoryPage.TITLE)
    assert title == "Products"

    # 2. Validar que hay productos
    assert actions.is_visible(InventoryPage.ITEMS)

    # 3. Obtener nombre y precio del primero
    name = actions.get_text(InventoryPage.FIRST_ITEM_NAME)
    price = actions.get_text(InventoryPage.FIRST_ITEM_PRICE)

    assert name != ""
    assert "$" in price


#Test validar agregar productos al carrito 

def test_add_to_cart(login):
    driver = login
    actions = Actions(driver)

    # 1. Agregar primer producto
    actions.click(InventoryPage.ADD_FIRST_ITEM)

    # 2. Validar contador del carrito
    badge = actions.get_text(InventoryPage.CART_BADGE)
    assert badge == "1"

    # 3. Ir al carrito
    actions.click(InventoryPage.CART_ICON)

    # 4. Validar que hay productos en el carrito
    assert actions.is_visible(CartPage.CART_ITEMS)

