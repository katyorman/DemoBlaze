from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class DemoBlazePage:
    # Boton login
    boton_login = (By.ID, "signin2")

    def __init__(self, driver):
        self.driver = driver

    def set_boton_login(self):
        pass  # Aquí debes implementar la lógica para interactuar con el botón de login

class TestDemoBlaze:
    driver = None

    @classmethod
    def setup_class(cls):  # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

    def test_pagina_principal(self):
        self.driver.get("https://www.demoblaze.com")

    @classmethod
    def teardown_class(cls):  # Método para cerrar el navegador después de todas las pruebas
        cls.driver.quit()
