# Pre Entrega Automation Testing - Saucedemo

Este proyecto automatiza flujos básicos de testing en la web saucedemo.com utilizando Selenium, Pytest y Python.

Se validan:
- Login
- Catálogo de productos
- Carrito de compras

Ademas dentro de la carpeta Utils se separaron las acciones/ funciones y los locators en otro archivo.

Los tests se agruparon todos en el archivo test_saucedemo y se agrego el reporte como se solicito

# Tecnologias 
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML

# Instalacion 

pip install -r requirements.txt

# Ejecucion 

pytest -v --html=reports/reporte.html
