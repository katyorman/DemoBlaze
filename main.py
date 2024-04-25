from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoBlazePage:
    # Boton login
    boton_login = (By.XPATH, '//*[@id="login2"]')
    click_agregar_nombre_login = (By.XPATH, '//*[@id="loginusername"]')
    agregar_contrasena_login = (By.XPATH, '//*[@id="loginpassword"]')
    click_boton_login = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    signup_username = (By.XPATH, '//*[@id="sign-username"]')
    boton_signin = (By.XPATH, '//*[@id="signin2"]')
    agregar_nombre = (By.XPATH, '//*[@id="sign-username"]')
    agregar_contrasena = (By.XPATH, '//*[@id="sign-password"]')
    click_signin = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
    producto = (By.XPATH, '//*[@id="tbodyid"]/div[1]/div')
    cerrar_popup = (By.XPATH, '//*[@id="signInModal"]/div/div/div[1]/button')

    def __init__(self, driver):
        self.driver = driver

    def set_boton_signin(self):
        self.driver.find_element(*self.boton_signin).click()

    def set_agregar_nombre(self, user_name):
        self.driver.find_element(*self.agregar_nombre).send_keys(data.user_name)

    def set_agregar_contrasena(self, password):
        self.driver.find_element(*self.agregar_nombre).send_keys(data.password)

    def set_boton_login(self):
        self.driver.find_element(*self.boton_login).click()
    def set_click_nombre_login(self):
        self.driver.find_element(*self.click_agregar_nombre_login).click()

    def set_click_contrasena_login(self):
        self.driver.find_element(*self.click_agregar_nombre_login).click()

class TestDemoBlazePage:
    driver = None

    @classmethod
    def setup_class(cls):
        # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.demo_blaze_url)
        cls.routes_page = DemoBlazePage(cls.driver)

    def test_boton_signin(self):
        routes_page = DemoBlazePage(self.driver)

        # Hacer clic en el botón "Sign In"
        self.driver.find_element(*routes_page.boton_signin).click()

        # Esperar a que el campo para agregar nombre esté disponible
        agregar_nombre = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.agregar_nombre)
        )
        # Una vez que el campo para agregar nombre esté disponible, enviar el nombre de usuario
        agregar_nombre.send_keys(data.user_name)

        # Esperar a que el campo para agregar contraseña esté disponible
        agregar_contrasena = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.agregar_contrasena)
        )
        # Una vez que el campo para agregar contraseña esté disponible, enviar la contraseña
        agregar_contrasena.send_keys(data.password)

        # Hacer clic en el botón "Sign In"
        self.driver.find_element(*routes_page.click_signin).click()

        # Esperar a que aparezca el cuadro de diálogo de alerta
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        time.sleep(5)

        self.driver.find_element(*routes_page.cerrar_popup).click()
        time.sleep(5)
    def test_login_page(self):
        routes_page = DemoBlazePage(self.driver)

        # Hacer clic en el botón "Sign In"
        self.driver.find_element(*routes_page.boton_login).click()
        time.sleep(2)
        # Esperar a que el campo para agregar nombre esté disponible
        click_agregar_nombre_login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.click_agregar_nombre_login)
        )
        # Una vez que el campo para agregar nombre esté disponible, enviar el nombre de usuario
        click_agregar_nombre_login.send_keys(data.user_name)
        time.sleep(2)
        # Esperar a que el campo para agregar contraseña esté disponible
        agregar_contrasena_login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.agregar_contrasena_login)
        )
        # Una vez que el campo para agregar contraseña esté disponible, enviar la contraseña
        agregar_contrasena_login.send_keys(data.password)
        time.sleep(2)
        self.driver.find_element(*routes_page.click_boton_login).click()
        time.sleep(2)
    @classmethod
    def teardown_class(cls):
        # Método para cerrar el navegador después de todas las pruebas
        cls.driver.quit()