import keyboard
import time
import Key_Binds as kb

class Blasters_True:
    @staticmethod
    # Função que será chamada quando a tecla for precionada
    def dlight_sair():
        print(f"Você apertou {kb.key2}, enviando D_light + S_air...")
        #Tecla que o progama vai apertar
        keyboard.press(f"{kb.Down} + {kb.Light_atack}")
        time.sleep(0.016)
        keyboard.release(f"{kb.Down} + {kb.Light_atack}")
        time.sleep(0.71)
        keyboard.press_and_release(f"{kb.Jump} + {kb.Light_atack}")
