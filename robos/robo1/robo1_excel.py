from lib2to3.pgen2 import driver
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd # para ler os dados do excel
from info import data

# variaveis
dominios = []
arquivo = open("resultado.txt","w")

# lendo do excel
workbook = xlrd.open_workbook(data.info)
sheet = workbook.sheet_by_index(0)
for linha in range(0,10):
    dominios.append(sheet.cell_value(linha,0)) # inserindo na lista os dados do arquivo excel linha x, coluna 0

print("Iniciando nosso robô...\n")
driver = webdriver.Chrome(data.cDriver)
driver.get("https://registro.br/")

# buscando os resultados
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("strong")
    texto = "Domínio %s %s \n" % (dominio, resultados[4].text)
    arquivo.write(texto) 
print("guardando resultados da pesquisa no arquivo...")
time.sleep(3)

# import pdb; pdb.set_trace() - pausa a automação para procurarmos um elemento (resultado)
arquivo.close()
driver.close()