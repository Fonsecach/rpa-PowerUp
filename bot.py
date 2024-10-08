from time import sleep
import pandas as pd
from utils.utils import open_app
import pyautogui as pg

x = 1052
y = 433

products = pd.read_csv('produtos.csv')

def login():
    open_app()
    sleep(2)
    pg.click(x, y)
    pg.press('f6')
    #pg.hotkey('ctrl', 'l')
    pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pg.press('enter')
    sleep(0.5)
    pg.click(1228,399)
    sleep(0.5)
    pg.write('email@example.com')
    sleep(1)
    pg.press('tab')
    sleep(1)
    pg.write('senha-segura')
    pg.press('enter')


def insert_products():
    for row in products.index:
        pg.click(1142, 296)
        sleep(0.5)
        codigo = products.loc[row, "codigo"]
        pg.write(str(codigo))
        pg.press('tab')
        pg.write(str(products.loc[row, "marca"]))
        pg.press("tab")
        pg.write(str(products.loc[row, "tipo"]))
        pg.press("tab")
        pg.write(str(products.loc[row, "categoria"]))
        pg.press("tab")
        pg.write(str(products.loc[row, "preco_unitario"]))
        pg.press("tab")
        sleep(2)
        pg.write(str(products.loc[row, "custo"]))
        pg.press("tab")
        obs = products.loc[row, "obs"]
        if not pd.isna(obs):
            pg.write(str(products.loc[row, "obs"]))
        pg.press("tab")
        sleep(1)
        try:
            for _ in range(3):
                pg.press('enter')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
        sleep(0.5)
        pg.scroll(5000)
