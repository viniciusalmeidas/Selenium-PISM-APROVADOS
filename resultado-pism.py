from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from sys import exit
import os 
import numpy as np

""" Esse programa utiliza Selenium em Python para coletar o nome dos aprovados no PISM no triênio 2019-2021, desenvolvido dia 17-04-2021. Utiliza a mesma lógica criada pelo autor VINICIUS ALMEIDA @viniciusalmeidas(GitHub) no Projeto Brasil-Brokers. 
"""

def main():
    # ESCOLHE O Ano da busca
    ano = 2022
    # ESCOLHE O CAMPUS
    campus='jf'
    # SETAGEM do Loop para os grupos
    groupsWeb=[11,20,12,19,13,14,21,15,22] #A 11 , A1 20 , B 12 , B1 19, C 13; D 14 , D1 21, E 15 , E1 22
    
    
    path = os.getcwd().replace("\\","/")+'/chromedriver.exe'#Caminho do ChromeDriver
    options = Options()
    options.add_argument("start-maximized")    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #Caminho para o ChromeDriver    
    
    #DAR NUMERO AO CAMPUS
    n_campus=0
    if campus == 'gv':
        n_campus = 6190
        inicio = 457
        fim = 570

    elif campus == 'jf':
        n_campus = 3087
        inicio = 519
        fim = 529
    
    for c in range(inicio,fim):#457 - 570(Juiz de fora) #519- 529 (Governador Valadares)
        #JF ARTES VISUAIS 564 e 565
        #JF CINEMA 566
        #JF DESIGN 567
        #JF MODA 568
        #JF ENFERMAGEM 569 
        for z in groupsWeb:
            try:          
                driver.get(f'http://www4.vestibular.ufjf.br/{ano}/resultadofinalpism3/aprovados_listagem_{n_campus}_{c}_{z}.html')
                sleep(1.5) 
                driver.refresh() 
                quantidade = len(driver.find_elements(by=By.XPATH, value='//*[@id="example"]/tbody/tr')) #número de aprovados na página        
                grupo = driver.find_element(by=By.XPATH, value='//*[@id="conteudo"]/div[1]/div[2]/div/div/div/table/tbody/tr[3]/td[2]').text #nome do grupo
                curso = driver.find_element(by=By.XPATH, value='//*[@id="conteudo"]/div[1]/div[2]/div/header/p').text #nome do curso
                #Criar Listas(vetores) vazios ou completos
                cursos=[]
                for i in range (0, quantidade):
                    cursos.append(curso)

                grupos=[]
                for i in range (0, quantidade):
                    grupos.append(grupo)
            
                nomes=[]
                inscricoes=[]
                totalPontos=[]
                classificacoes=[]
                situacoes=[]
                

                #Loop nos alunos na página
                for i in range(1,quantidade+1): 
                    nome = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td[2]').text
                    inscricao = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td[3]').text
                    pontos = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td[4]').text
                    classificacao = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td[5]').text
                    situacao = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td[6]').text
                    
                    #Adicionar linha com aluno nos vetores criados
                    nomes.append(nome)
                    inscricoes.append(inscricao)
                    totalPontos.append(pontos)
                    classificacoes.append(classificacao)
                    situacoes.append(situacao)

                #Juntar lista na transposta
                linhas = list(zip(*[cursos,grupos, nomes, inscricoes, totalPontos, classificacoes,situacoes]))

                #Escrever em arquivo CSV
                filename = f'{c}-{curso.split()[0]}-{grupos[0]}.csv'
            
                f = open(filename, "w") #Abrir arquivo
                headers = "Curso, Grupo, Nome, Inscrição, Total de Pontos, Total de Pontos2, Classificação, Situação\n" #Cabeçalho
                f.write(headers) #Escrever Cabeçalho
                
                for i in range(0,quantidade):
                    f.write(f'{linhas[i]}\n') #Escrevendo no arquivo csv
                
                f.close() #Fechar arquivo  
                driver.refresh()
                print(filename)

            except Exception: #Tratamento de Erro
                driver.refresh()
                print(f'Sem Alunos aprovados no curso: {c} - {grupo}' )
    
    print(f'FIM do {grupo}!')
    
                
        


if __name__ == '__main__':
    main()






