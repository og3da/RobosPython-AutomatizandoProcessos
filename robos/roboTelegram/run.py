from TelegramBot import TelegramBot
# rodar o bot 
obj_telegram =  TelegramBot()

print("Iniciando o robô...")
grupo_alvo = obj_telegram.get_groups()
membros = obj_telegram.get_members_group(grupo_alvo)
print(f'{membros} membros encontrados no grupo alvo')

print("")
print("Escolha o grupo a adicionar os membros")
meu_grupo = obj_telegram.get_groups()

for membro in membros:
    adicionado = obj_telegram.add_member_toGroup(membro, meu_grupo)
    if adicionado:
        print(f"membro {membro.id} adicionado")
