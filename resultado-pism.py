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
    path = os.getcwd().replace("\\","/")+'/chromedriver.exe'#Caminho do ChromeDriver
    driver = webdriver.Chrome(executable_path=path) #Caminho para o ChromeDriver    
    
    for c in range(519,529):#457 - 518(Juiz de fora) #519, 529 (Governador Valadares)

        try:
            #3087 - JUIZ DE FORA e #6190 - GOVERNADOR VALADARES
            driver.get(f'http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_listagem_6190_{c}_11.html')
            # Loop para os grupos
            # A 11 , A1 20  
            # B 12 , B1 19
            # C 13;
            # D 14 , D1 21
            # E 15 , E1 22
            sleep(2.5) #tempo de carregamento 
            quantidade = len(driver.find_elements_by_xpath('//*[@id="example"]/tbody/tr')) #número de aprovados na página        
            grupo = driver.find_element_by_xpath('//*[@id="conteudo"]/div[1]/div[2]/div/div/div/table/tbody/tr[3]/td[2]').text #nome do grupo
            curso = driver.find_element_by_xpath('//*[@id="conteudo"]/div[1]/div[2]/div/header/p').text #nome do curso
            
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
                nome = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[2]').text
                inscricao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[3]').text
                pontos = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[4]').text
                classificacao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[5]').text
                situacao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[6]').text
                
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
                f.write(f'{linhas[i]}\n') 
            
            f.close() #Fechar arquivo  

        except Exception: #Tratamento de Erro
                sleep(2)
                print("Deu erro!")
                
        

if __name__ == '__main__':
    main()







