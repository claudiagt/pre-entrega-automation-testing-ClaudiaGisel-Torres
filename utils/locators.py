from selenium.webdriver.common.by import By



#clase login

class LoginPage:
    # Campo usuario
    USERNAME = (By.ID, "user-name")

    # Campo contraseña
    PASSWORD = (By.ID, "password")

    # Botón login
    LOGIN_BTN = (By.ID, "login-button")



#clase lista de productos

class InventoryPage:
    # Título "Products"
    TITLE = (By.CLASS_NAME, "title")

    # Lista de productos
    ITEMS = (By.CLASS_NAME, "inventory_item")

    # Primer producto (nombre y precio)
    FIRST_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

#Locators test agregar items al carrito

   # Botón "Add to cart" del primer producto
    ADD_FIRST_ITEM = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")

    # Contador del carrito 
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Icono del carrito
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

#clase carrito 

class CartPage:
    # Productos dentro del carrito
    CART_ITEMS = (By.CLASS_NAME, "cart_item")