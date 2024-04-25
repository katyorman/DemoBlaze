from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import data
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoBlazePage:
    # Boton login
    boton_login = (By.XPATH, '//*[@id="login2"]')
    signup_username = (By.XPATH, '//*[@id="sign-username"]')
    boton_signin = (By.XPATH, '//*[@id="signin2"]')
    producto = (By.XPATH, '//*[@id="tbodyid"]/div[1]/div')
    agregar_nombre = (By.XPATH, '//*[@id="sign-username"]')
    agregar_contrasena = (By.XPATH, '//*[@id="sign-password"]')
    click_signin = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    def __init__(self, driver):
        self.driver = driver

    def set_boton_signin(self):
        self.driver.find_element(*self.boton_signin).click()
    def set_agregar_nombre(self, user_name):
        self.driver.find_element(*self.agregar_nombre).send_keys(data.user_name)
    def set_agregar_contrasena(self, password):
        self.driver.find_element(*self.agregar_nombre).send_keys(data.password)

class TestDemoBlaze:
    driver = None

    @classmethod
    def setup_class(cls):  # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.demo_blaze_url)
        cls.routes_page = DemoBlazePage(cls.driver)

    def test_boton_signin(self):
        routes_page = DemoBlazePage(self.driver)
        self.driver.find_element(*routes_page.boton_signin).click()
        time.sleep(3)
        self.driver.find_element(*routes_page.agregar_nombre).send_keys(data.user_name)
        self.driver.find_element(*routes_page.agregar_contrasena).send_keys(data.password)
        time.sleep(3)
        self.driver.find_element(*routes_page.click_signin).click()
        time.sleep(3)

    @classmethod
    def teardown_class(cls):  # Método para cerrar el navegador después de todas las pruebas
        cls.driver.quit()
