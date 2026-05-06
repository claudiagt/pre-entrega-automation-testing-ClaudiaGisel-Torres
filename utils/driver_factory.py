from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Configuración del navegador
    options = Options()
    
    # Abrir maximizado (evita problemas de elementos fuera de pantalla)
    options.add_argument("--start-maximized")

    # Crear el driver
    driver = webdriver.Chrome(options=options)

    # Espera implícita (backup)
    driver.implicitly_wait(5)

    return driver