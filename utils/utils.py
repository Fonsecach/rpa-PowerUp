import pyautogui as pg
from time import sleep

def open_app():
    try:
        pg.hotkey('Super', 'F1')
        sleep(0.5)
    except Exception as e:
        print(f"Erro ao abrir o aplicativo: {e}")

