from re import U
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from info import data

# abrindo o navegador com uma pesquisa qualquer
pesquisa = input("Digite a informação a pesquisar: ")
driver = webdriver.Chrome(data.cDriver)
driver.get("https://google.com.br")

# encontrando o campo pesquisar do google por meio do xpath
campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

# capturando a quantidade de resultados encontrados (ex: 100 paginas encontradas)
resultados = driver.find_element_by_xpath("//*[@id='result-stats']").text
numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace(".",""))
maximo_paginas = numero_resultados/10
print(f'Número de páginas = {maximo_paginas}')

# navegando entre as paginas (ex: da pagina 1 ate a 10) e salvando em um arquivo de texto
lista_resultados = []
url_pagina = driver.find_element_by_xpath("//a[@aria-label='Page 2']").get_attribute("href")
pagina_atual = 0
paginas_percorrer = int(input(f"Páginas encontradas {maximo_paginas} \n Digite quantas paginas deseja percorrer: "))
start = 10
while pagina_atual <= paginas_percorrer-1:
    if pagina_atual > 1:
        url_pagina = url_pagina.replace(f'start={start}',f'start={start+10}')
        start += 10
        driver.get(url_pagina)
    elif pagina_atual == 1:
        driver.get(url_pagina)
    pagina_atual += 1

    # capturando titulo e link das paginas navegadas
    divs = driver.find_elements_by_xpath("//div[@class='yuRUbf']")
    for div in divs:
        nome = div.find_element_by_tag_name("h3")
        link = div.find_element_by_tag_name("a")
        resultado = f'titulo: {nome.text}, link:{link.get_attribute("href")}'
        print(resultado)
        print()
        lista_resultados.append(resultado)

with open("resultados.txt","w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write(f'{resultado}\n')
    arquivo.close()
print(f'{len(lista_resultados)} resultados encontrados do Google e salvos no arquivo')