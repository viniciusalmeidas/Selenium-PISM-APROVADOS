from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from sys import exit
import os
import numpy as np

""" Esse programa utiliza Selenium em Python para coletar o nome dos aprovados no PISM no triênio 2018-2020, desenvolvido dia 17-04-2021. Utiliza a mesma lógica criada pelo autor VINICIUS ALMEIDA @viniciusalmeidas(GitHub) no Projeto Brasil-Brokers. 
"""


def main():
    path = os.getcwd().replace("\\", "/")+'/chromedriver.exe'  # Caminho do ChromeDriver
    print(path)
    # Caminho para o ChromeDriver
    driver = webdriver.Chrome(executable_path=path)

    informacoes = []
    urls = []
    
    # try:
    driver.get(
        f'https://www2.ufjf.br/cdara/graduacao/matricula-graduacao/sisu/sisu-2020-1a-edicao/lista-de-espera-sisu-9/')
    sleep(2)
    quantidade = len(driver.find_elements_by_xpath(
        '//*[@id="conteudo"]/ul/li'))  # número de cursos na página

    for i in range(1, quantidade):
        url = driver.find_element_by_xpath(
            f'//*[@id="conteudo"]/ul/li[{i}]/a').get_attribute('href')
        urls.append(url)

    
    for url in urls:
        nomes = []
        cpfs = []
        pontos = []
        classificacoes = []
        situacoes = []
        linhas = []

        driver.get(f'{url}')  # Acessar a pagina do curso
        sleep(2)
        numeroAlunos = len(driver.find_elements_by_xpath(
            '//*[@id="sisu"]/tbody/tr'))
        informacao = driver.find_element_by_xpath(
                f'//*[@id="conteudo"]/h2').text

        # Loop nos alunos na página
        for aluno in range(2, numeroAlunos+1):
            classificacao = driver.find_element_by_xpath(
                f'//*[@id="sisu"]/tbody/tr[{aluno}]/td[1]').text
            nome = driver.find_element_by_xpath(
                f'//*[@id="sisu"]/tbody/tr[{aluno}]/td[2]').text
            cpf = driver.find_element_by_xpath(
                f'//*[@id="sisu"]/tbody/tr[{aluno}]/td[3]').text
            ponto = driver.find_element_by_xpath(
                f'//*[@id="sisu"]/tbody/tr[{aluno}]/td[4]').text
            situacao = driver.find_element_by_xpath(
                f'//*[@id="sisu"]/tbody/tr[{aluno}]/td[5]').text

            # Adicionar linha com aluno nos vetores criados
            informacoes.append(informacao)
            classificacoes.append(classificacao)
            nomes.append(nome)
            cpfs.append(cpf)
            pontos.append(ponto)
            situacoes.append(situacao)

        # Juntar lista na transposta
        linhas = list(zip(*[informacoes, classificacoes, nomes, cpfs, pontos, situacoes]))
                        
        # Escrever em arquivo CSV
        filename = f'{informacao}.csv'
        f = open(filename, "w") #Abrir arquivo
        headers = "Informacoes, Classificação, Nome, CPF, Total de Pontos,Situação\n" #Cabeçalho
        f.write(headers) #Escrever Cabeçalho
        for i in range(0,len(linhas)):
            f.write(f'{linhas[i]}\n')

        f.close() #Fechar arquivo

    # except Exception:
            # sleep(2)
            # print(f'Deu erro! {numeroAlunos}{url}')


if __name__ == '__main__':
    main()
