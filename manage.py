from utils.logar.login import Login
from selenium import webdriver
from utils.interact.followers.follow import User
from utils.interact.direct.sell_msg import Mensage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time
import random
'''
voce vai precisar criar uma função pra cada item do menu
exemplo ciclo completo chama a funcao ciclo completo
seguir chama a funcao seguir
'''


def date_hours():
    now = datetime.now()
    return format(now,"%d-%m-%Y_%H-%M-%S")

def follow_now(driver, user_follow):
    try:
        with open('chaos/data_base/leads.txt', 'r') as file:
            links = [line.strip() for line in file]

        for link in links:
            print(f'\nAcessando {link}')
            driver.get(link)
            time.sleep(3)  # Espera para garantir que a página seja carregada

            driver.implicitly_wait(10)

            try:
                # Verifica a presença do elemento
                not_found = driver.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xbxaen2 x1u72gb5 x1t1ogtf x13zrc24 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh xl56j7k"]')
                if not_found:
                    print(f'{link} não encontrado, acessando o próximo perfil da lista')
                    continue
            except NoSuchElementException:
                driver.implicitly_wait(10)
                user_follow.follow(driver)
                print('Saí da função e estou indo salvar o nome na lista')
                with open('chaos/data_base/seguindo.txt', 'a', encoding='utf-8') as list_follow:
                    list_follow.write(link + '\n')
                    print(f'Salvei o usuário {user_follow.name} na lista')
                    name_direct = user_follow.name
                    time.sleep(random.randint(1, 3))
                    Mensage().send_msg(driver, name_direct)
                    print('Indo para o próximo usuário')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Encerrando a lista')

def unfollow_now(driver,user_follow):#tratamento conta privada
    with open('chaos/data_base/seguindo.txt','r') as list:
        for i in list:
            link = i.strip()
            driver.get(link)
            print(f'\nAcessando {link}')
            time.sleep(3)
            driver.implicitly_wait(10)

            try:
                not_found = driver.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xbxaen2 x1u72gb5 x1t1ogtf x13zrc24 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh xl56j7k"]')
                if not_found:
                    print(f'{link} nao encontrado, acessando o proximo perfil da lista')
                    continue
            except NoSuchElementException:
                driver.implicitly_wait(10)
                user_follow.unfollow(driver)
                print('sai da funcao e estou indo salvar o nome na lista')
                with open('chaos/data_base/deixou_seguir.txt','a',encoding='utf-8') as list_unfollow:
                    list_unfollow.write(link + '\n')
                    print(f'Salvei o usuario {user_follow.name} na lista')
            

driver = webdriver.Firefox()
user = '_ratcode'
password = '87689610'
print('\n Aguarde...')
entry_acount = Login(user,password)
entry_acount.logining(driver)
user_follow = User()
follow_now(driver,user_follow)
#unfollow_now(driver,user_follow)




            



print('\nEncerrando o programa')













#curtir as fotos
#enviar as msg


