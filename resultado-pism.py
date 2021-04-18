from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from sys import exit
import os 
import numpy as np





def main():
    path = os.getcwd().replace("\\","/")+'/chromedriver.exe'#Caminho do ChromeDriver
    driver = webdriver.Chrome(executable_path=path) #Escrever Cabeçalho    

    
    for c in range(457,519):#457 - 518

        try:
            #3087 - JUIZ DE FORA 
            #6190 - GOVERNADOR VALADARES
            driver.get(f'http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_listagem_6190_{c}_15.html') #Página para entrar GRUPO D
            sleep(2.5)
            quantidade = len(driver.find_elements_by_xpath('//*[@id="example"]/tbody/tr'))        
            grupo = driver.find_element_by_xpath('//*[@id="conteudo"]/div[1]/div[2]/div/div/div/table/tbody/tr[3]/td[2]').text
            curso = driver.find_element_by_xpath('//*[@id="conteudo"]/div[1]/div[2]/div/header/p').text

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

            for i in range(1,quantidade+1):
                nome = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[2]').text
                inscricao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[3]').text
                pontos = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[4]').text
                classificacao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[5]').text
                situacao = driver.find_element_by_xpath(f'//*[@id="example"]/tbody/tr[{i}]/td[6]').text

                nomes.append(nome)
                inscricoes.append(inscricao)
                totalPontos.append(pontos)
                classificacoes.append(classificacao)
                situacoes.append(situacao)
    
        
            linhas = list(zip(*[cursos,grupos, nomes, inscricoes, totalPontos, classificacoes,situacoes]))
        
            filename = f'{c}-{curso.split()[0]}-{grupos[0]}.csv'
            f = open(filename, "w") #Abrir arquivo
            headers = "Curso, Grupo, Nome, Inscrição, Total de Pontos, Total de Pontos2, Classificação, Situação\n" #Cabeçalho
            f.write(headers) #Escrever Cabeçalho
            for i in range(0,quantidade):
                f.write(f'{linhas[i]}\n') 
            
            f.close() #Fechar arquivo  

        except Exception:
                sleep(2)
                print("Deu erro!")
                
        

if __name__ == '__main__':
    main()







