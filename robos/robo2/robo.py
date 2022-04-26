from re import U
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from info import data

pesquisa = input("Digite a informação a pesquisar: ")
driver = webdriver.Chrome(data.cDriver)
driver.get("https://google.com.br")

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element_by_xpath("//*[@id='result-stats']").text
numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace(".",""))
maximo_paginas = numero_resultados/10
print(f'Número de páginas = {maximo_paginas}')

url_pagina = driver.find_element_by_xpath("//a[@aria-label='Page 2']").get_attribute("href")
pagina_atual = 0
start = 10
while pagina_atual <= 10:
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace(f'start={start} , start={start+10}')
        start += 10
    pagina_atual += 1
    driver.get(url_pagina)