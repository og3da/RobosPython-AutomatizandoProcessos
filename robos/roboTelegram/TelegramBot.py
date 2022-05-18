import telethon # biblioteca para utilizar funções do Telegram 
import time
from config import api_id, api_hash, phone

class TelegramBot:
    def __init__(self):
        # passando as credenciais necessarias da API telegram
        self.api_id   = api_id
        self.api_hash = api_hash
        self.phone    = phone
        self.client = telethon.TelegramClient(self.phone, self.api_id, self.api_hash)
        self.connect()

    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input("Digite o código: "))
        return True