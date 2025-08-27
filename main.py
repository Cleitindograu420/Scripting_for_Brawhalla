import keyboard

#importa a lista de combos
from All_combos import Blasters,Axe

#imposta a lista de key binds
import Key_Binds as kb

# Associa a tecla ao evento
#Ainda não entendi como o Lambda funciona aqui
keyboard.on_press_key(kb.key1, lambda _: Axe.Axe_True.slight_dlight_Axe())
keyboard.on_press_key(kb.key2, lambda _: Blasters.Blasters_True.dlight_sair())

#Apertar key0 para o progama
print(f"Programa rodando. Pressione {kb.key0} para sair.")
keyboard.wait(kb.key0)
