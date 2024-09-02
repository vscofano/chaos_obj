from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time



class TestDriver:
    def __init__(self):
        pass

    def find_element(self,xpath,css,fullXpath,driver):
        locators = [
            (By.XPATH,xpath),
            (By.CSS_SELECTOR,css),
            (By.XPATH,fullXpath)
        ]

        for by,value in locators:
            try:
                element = driver.find_element(by,value)
                return element
            except NoSuchElementException:
                continue
        raise NoSuchElementException(f"Element not found with any of the provided selectors: {locators}")
  
    def conection_testing(self,url,driver):
        driver.get(url)
        driver.implicitly_wait(10)
        c = 0
        while c <= 5:
             response = requests.get(url)
             c += 1
             if response.status_code == 200:
                 print(f'Entrando em {url}')
                 break
             else:
                 print(f'Falha na Conexão. Erro {response}. Vou tentar conectar Novamente')


    '''    try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"Connection failed: {e}")
            return False'''


