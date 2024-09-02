from utils.testing.test import TestDriver
import time
import random

class User:
    def __init__(self):
       self.name = None
       

    def follow(self,driver):
        list_adress = [[#user_name
        '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[4]/div/div[1]/span',
                '.x1amjocr > span:nth-child(1)',
                ''
            ],
            [#btn_follow
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div[2]/div/div[1]/button/div/div',
                'div._ap3a',
                ''
            ]
        ]
        self.name = TestDriver().find_element(list_adress[0][0],list_adress[0][1],list_adress[0][2],driver).text
        print(self.name)
        btn_follow = TestDriver().find_element(list_adress[1][0],list_adress[1][1],list_adress[1][2],driver)
        if btn_follow.text != 'Following':
            btn_follow.click()
            print(f'Seguindo {self.name}')
            time.sleep(random.randint(1,3))
 
    
    def unfollow(self,driver):
        list_adress = [[#box_btn
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button',
                '._acan',
                ''
            ],
            [#btn_unfollow
                '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]',
                'div.x1i10hfl:nth-child(8) > div:nth-child(1)',
                ''
            ],
            [#user_name
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[4]/div/div[1]/span',
                '.x1amjocr > span:nth-child(1)',
                ''
            ]
        ]
        self.name = TestDriver().find_element(list_adress[2][0],list_adress[2][1],list_adress[2][2],driver).text
        print(self.name)
        box_unfollow = TestDriver().find_element(list_adress[0][0],list_adress[0][1],list_adress[0][2],driver)
        box_unfollow.click()
        time.sleep(2)
        driver.implicitly_wait(10)
        btn_unfollow = TestDriver().find_element(list_adress[1][0],list_adress[1][1],list_adress[1][2],driver)
        btn_unfollow.click()
        print(f'\n Unfollow {self.name}')
        time.sleep(2)






