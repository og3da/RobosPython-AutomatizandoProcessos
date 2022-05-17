from importlib.resources import path
import chromedriver_binary
from selenium import webdriver
import time
from info import data

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome(data.cDriver)
    
    def busca(self, pesquisa):
        videos = []
        pagina = 1

        url = f"https://www.youtube.com/results?search_query={pesquisa}"
        self.webdriver.get(url)

        while pagina <= 3:
            titulos = self.webdriver.find_elements_by_xpath("//a[@id='video-title']")
            for titulo in titulos:
                if titulo.text not in videos: # validação para nao haver duplicidade de titulos
                    print(f'titulo encontrado: {titulo.text}')
                    videos.append(titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1 

    def proxima_pagina(self, pagina):
        print(f'Mudando para a pagina {pagina +1}')
        bottom = pagina * 10000 
        self.webdriver.execute_script(f"window.scrollTo(0, {bottom});") # função JS para rolar a página até o final e carregar os proximos videos
        time.sleep(7)

bot = RoboYoutube()
pesquisa = input("Digite a pesquisa a realizar: ")
bot.busca(pesquisa)
