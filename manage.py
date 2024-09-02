from utils.logar.login import Login
from selenium import webdriver
from utils.interact.followers.follow import User
from utils.interact.direct.sell_msg import Mensage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import random

def menu():
    print("\n" + "=" * 30)
    print("         MENU PRINCIPAL")
    print("=" * 30)
    print("| 1 - 📈  Seguir")
    print("| 2 - ✉️  Enviar Direct")
    print("| 3 - 🚫  Deixar de Seguir")
    print("| 4 - 🔄  Ciclo Completo")
    print("| 5 - 🛠  Suporte")
    print("=" * 30)
    
    opcao = input("Escolha uma opção (1-7): ")
    print("=" * 30)
    return opcao

def follow_now(driver,user_follow):
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
                    print('Indo para o próximo usuário')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Encerrando a lista')

def follow_now_direct(driver, user_follow):
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
                    Mensage().send_msg(driver)
                    print('Indo para o próximo usuário')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Encerrando a lista')

def unfollow_now(driver, user_follow):
    try:
        with open('chaos/data_base/seguindo.txt', 'r') as file:
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
                user_follow.unfollow(driver)
                print('Saí da função e estou indo salvar o nome na lista')
                with open('chaos/data_base/deixou_seguir.txt', 'a', encoding='utf-8') as list_unfollow:
                    list_unfollow.write(link + '\n')
                    print(f'Salvei o usuário {user_follow.name} na lista')
                    print('Indo para o próximo usuário')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Encerrando a lista')

def sell_direct_msg(driver):
    try:
        # Carrega os links do arquivo e remove linhas vazias
        with open('chaos/data_base/leads.txt', 'r') as file:
            links = [line.strip() for line in file if line.strip()]

        # Verifica se a lista de links está vazia
        if not links:
            print('A lista de links está vazia. Verifique o arquivo leads.txt.')
            return

        # Processa cada link na lista
        for link in links:
            # Verifica se a URL é válida
            if not (link.startswith("http://") or link.startswith("https://")):
                print(f"URL inválida: '{link}', pulando para o próximo.")
                continue

            print(f'\nAcessando {link}')
            try:
                driver.get(link)
                time.sleep(3)  # Espera para garantir que a página seja carregada
                driver.implicitly_wait(10)

                try:
                    # Verifica a presença do elemento "não encontrado"
                    not_found = driver.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xbxaen2 x1u72gb5 x1t1ogtf x13zrc24 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh xl56j7k"]')
                    if not_found:
                        print(f'{link} não encontrado, acessando o próximo perfil da lista')
                        continue
                except NoSuchElementException:
                    # Se o elemento "não encontrado" não estiver presente, envia a mensagem
                    Mensage().send_msg(driver)
                    time.sleep(random.randint(1,3))
                    print('Já enviei a mensagem e estou indo para o próximo da lista')

            except Exception as e:
                print(f'Erro ao acessar {link}: {e}')
                continue

    except FileNotFoundError:
        print('Arquivo leads.txt não encontrado. Verifique o caminho e tente novamente.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Encerrando a lista')



opcao_escolhida = menu()
driver = webdriver.Firefox()
user_follow = User()
user = input('Digite o Nome de Usuario \n')
password = input('Digite a senha \n')
print('\n Aguarde...')
entry_acount = Login(user,password)
entry_acount.logining(driver)

if opcao_escolhida == "1":
    print("📈 Você escolheu: Seguir")
    print('\n Aguarde...')
    follow_now(driver,user_follow)

elif opcao_escolhida == "2":
    print("✉️ Você escolheu: Enviar Direct")
    print('\n Aguarde...')
    sell_direct_msg(driver)
elif opcao_escolhida == "3":

    print("🚫 Você escolheu: Deixar de Seguir")
    print('\n Aguarde...')
    unfollow_now(driver,user_follow)

elif opcao_escolhida == "4":
    print("🔄 Você escolheu: Ciclo Completo")
    print('\n Aguarde...')
    follow_now_direct(driver,user_follow)

elif opcao_escolhida == "5":
    print("🛠 Você escolheu: Suporte \n Entre em contato comigo no numero (31)97150-2217) para ser atendido")

else:
    print("Opção inválida. Por favor, escolha um número de 1 a 7.")


print('\nEncerrando o programa')
driver.quit()






