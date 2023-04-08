# Importamos el módulo unittest y la biblioteca Selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Definimos la clase de prueba, que hereda de TestCase
class CalificacionDeAnime(unittest.TestCase):

    # Este método se ejecuta antes de cada prueba
    def setUp(self):
        # Creamos una instancia del controlador de Selenium para el navegador Edge
        self.driver = webdriver.Edge()

    # Esta es la prueba propiamente dicha
    def test_calificar_anime(self):
        # Simulamos el inicio de sesión en el sitio web myanimelist.net
        self.driver.get("https://myanimelist.net/login.php")
        self.driver.fullscreen_windows()
        username = self.driver.find_element(By.ID,"loginUserName")
        password = self.driver.find_element(By.ID,"login-password")
        username.send_keys("Beiacox")
        password.send_keys("esta no es la contraseña")
        # Tomamos una captura de pantalla
        self.driver.get_screenshot_as_file("img/"+self.driver.name+".png")
        login_button = self.driver.find_element(By.CSS_SELECTOR,".btn-recaptcha-submit")
        login_button.click()

        # Navegamos a la página del perfil de usuario
        self.driver.get("https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood")
        # Tomamos otra captura de pantalla
        self.driver.get_screenshot_as_file(self.driver.name+".png")

        # Seleccionamos la puntuación de 9 para un anime
        rating_9 = self.driver.find_element(By.XPATH,"//li[text()='9']")
        # Tomamos otra captura de pantalla
        self.driver.get_screenshot_as_file(self.driver.name+"2"+".png")
        rating_9.click()

        # Guardamos la calificación
        save_button = self.driver.find_element(By.CSS_SELECTOR,".button_save")
        save_button.click()

        # Verificamos que se muestra el mensaje de confirmación correcto
        confirmation_message = self.driver.find_element(By.CSS_SELECTOR,".message")
        self.assertEqual(confirmation_message.text, "Your score of 9 has been saved.")
        # Tomamos una última captura de pantalla
        self.driver.get_screenshot_as_file(self.driver.name+"3"+".png")

    # Este método se ejecuta después de cada prueba
    def tearDown(self):
        # Cerramos el navegador
        self.driver.quit()

# Verificamos si este archivo es el programa principal
if __name__ == '__main__':
    # Ejecutamos todas las pruebas definidas en la clase CalificacionDeAnime
    unittest.main()