from utils.testing.test import TestDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import time


class Mensage:
    def __init__(self):
       pass


    def send_msg(self,driver,name_direct):#adicionar classe e id
        list_adress = [[#btn_direct
  '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]/div',

            '.x10w6t97',  
            '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]'

        ],

        [#area_text
            '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]',

            'div.xzsf02u',
            ''

        ],

        [#send
            '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]',

            'div.xjqpnuy:nth-child(3)',

            ''
        ]
        ]
        list_msg = [
    'abora brinha com abobrinha faz um lanche de abobrinha',
    'o peito do pe do pedro e preto, qual a cor do peito do pe do pedro',
    'agua mole em pedra dura tanto bate ate que fura'
]
        mensagem = list_msg[random.randint(0,3)]
        btn_direct = TestDriver().find_element(list_adress[0][0],list_adress[0][1],list_adress[0][2],driver)
        btn_direct.click()
        print(f'indo para o direct {name_direct}')
        time.sleep(random.randint(1,3))
        driver.implicitly_wait(10)
        area_direct = TestDriver().find_element(list_adress[1][0],list_adress[1][1],list_adress[1][2],driver)
        area_direct.click()
        for car in mensagem:
            area_direct.send_keys(car)
            time.sleep(0.2)
        try: 
            send = TestDriver().find_element(list_adress[2][0],list_adress[2][1],list_adress[2][2],driver)
            if send:
                send.click()
                print('Mensagem Enviada')
        except NoSuchElementException:
            area_direct.send_keys(Keys.ENTER)
            print('Mensagem Enviada')












#se a conta for privada pula pra proxima, conferir antes da chamar a funcao msg
'''
fazendo o usuario digitar a mensagem
for i in range(3):
    user_message = input(f'Digite a mensagem {i + 1}: ')
    my_list.append(user_message)'''


