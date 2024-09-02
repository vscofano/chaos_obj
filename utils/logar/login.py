from utils.testing.test import TestDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def logining(self,driver):
        url = 'https://www.instagram.com/accounts/login/?source=logged_out_homepage'
        TestDriver().conection_testing(url,driver)
        time.sleep(10)
        list_adress =[[#input_login
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[1]/div/label/input',
                '#loginForm > div > div:nth-child(1) > div > label > input',
                '//*[@id="loginForm"]/div/div[1]/div/label/input'],
            [#input password
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[2]/div/label/input',
                '#loginForm > div > div:nth-child(2) > div > label > input',
                '//*[@id="loginForm"]/div/div[2]/div/label/input'
            ],
            [#senha incorreta
                '//div[@class="_ab2z"]',
                '._ab2z',
                ''
            ]
        ]
        input_login = TestDriver().find_element(*list_adress[0],driver)
        input_login.clear()
        input_login.send_keys(self.username)
        time.sleep(1)

        input_password = TestDriver().find_element(*list_adress[1],driver)
        input_password.clear()
        input_password.send_keys(self.password)
        time.sleep(1)
        input_password.send_keys(Keys.ENTER)
        time.sleep(2)
        print('login feito com sucesso\n')
        # Verificação de erros de login,criar uma função e tirar o self.username
        list_popup = [#btn_unfollow
                '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]',
                'button._a9--:nth-child(2)',
                '' 
        ]
        btn_unfollow = TestDriver().find_element(*list_popup,driver)
        btn_unfollow.click()
        print('Popup Fechado ')



