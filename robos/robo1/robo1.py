from lib2to3.pgen2 import driver
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from info import data

print("Iniciando nosso robô...\n")
driver = webdriver.Chrome(data.cDriver)
driver.get("https://registro.br/")

dominios = ["roboscompython.com.br","udemy.com.br","uol.com.br","pythoncurso.com"]
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("strong")
    print("Domínio %s %s" % (dominio, resultados[4].text))   

# import pdb; pdb.set_trace() - pausa a automação para procurarmos um elemento (resultado)
driver.close()