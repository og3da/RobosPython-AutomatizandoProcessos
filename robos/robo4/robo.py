from importlib.resources import path
import chromedriver_binary
from selenium import webdriver
import time
from info import data

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome(data.cDriver)
    
    def busca(self, pesquisa):
        url = f"https://www.youtube.com/results?search_query={pesquisa}"
        self.webdriver.get(url)
        titulos = self.webdriver.find_elements_by_xpath("//a[@id='video-title']")
        for titulo in titulos:
            print(f'titulo encontrado: {titulo.text}')

bot = RoboYoutube()
pesquisa = input("Digite a pesquisa a realizar: ")
bot.busca(pesquisa)
