from TelegramBot import TelegramBot
# rodar o bot 
obj_telegram =  TelegramBot()

print("Iniciando o robô...")
grupo_alvo = obj_telegram.get_groups()
membros = obj_telegram.get_members_group(grupo_alvo)