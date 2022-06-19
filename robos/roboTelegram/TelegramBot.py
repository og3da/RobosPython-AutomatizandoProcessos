from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import time
from config import api_id, api_hash, phone

class TelegramBot:
    def __init__(self):
        # passando as credenciais necessarias da API telegram
        self.api_id   = api_id
        self.api_hash = api_hash
        self.phone    = phone
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        self.connect()

    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input("Digite o código: "))
        return 

    def get_groups(self):
        groups = []

        chats = self.client(GetDialogsRequest(
            offset_date=None, 
            offset_id=0, 
            offset_peer=InputPeerEmpty(), 
            limit=200, 
            hash=0))
        
        for chat in chats.chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print("--- GRUPOS ---")
        print()
        i=1
        for group in groups:
            print(f'{i} - {group.title}')
            i += 1

        escolha = input("Escolha um grupo alvo: ")
        grupo_alvo = groups[int(escolha)-1]
        return grupo_alvo

    def get_members_group(self, target_group):
        all_participants = self.client.get_participants(target_group) 
        return all_participants

    def add_member_toGroup(self, user, target_group):
        target_group_entity = InputPeerChannel(target_group.id,  target_group.access_hash)


        try:
            print("Adicionando usuário %s" % user.id)

            user_to_add = InputPeerUser(user.id, user.access_hash)

            self.client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            time.sleep(2)
            return True

        except PeerFloodError:
            print("erro de flood. Sleep de 5min")
            time.sleep(300)
            return False

        except UserPrivacyRestrictedError:
            print("usuario nao permite ser adicionado")
            return False

        except Exception:
            print(f"Erro retornado: {str(Exception)}")
            return False
