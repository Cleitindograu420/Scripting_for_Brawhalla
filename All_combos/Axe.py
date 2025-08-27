import keyboard
import time
import Key_Binds as kb

class Axe_True:
    @staticmethod
    # Função que será chamada quando a tecla for precionada
    def slight_dlight_Axe():
        print(f"Você apertou {kb.key1}, enviando Side light + D_light...")
        #Tecla que o progama vai apertar
        keyboard.press_and_release(kb.Light_atack)
        time.sleep(0.53)
        keyboard.press(f"{kb.Down} + {kb.Light_atack}")
        time.sleep(0.016)
        keyboard.release(f"{kb.Down} + {kb.Light_atack}")
    