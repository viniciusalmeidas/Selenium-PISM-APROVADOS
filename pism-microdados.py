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
from locale import atof, setlocale, LC_NUMERIC

""" Esse programa utiliza Selenium em Python para coletar microdados do PISM no triênio, desenvolvido dia 06-09-2021. Utiliza a mesma lógica criada pelo autor VINICIUS ALMEIDA @viniciusalmeidas(GitHub). 
"""
setlocale(LC_NUMERIC, '')

def main():
    # letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    letras=["C"]
    #letras=["B","H","M","O","Q","T","U","W","Z"] 
    # letras=["A","E","R","S","V"] 
    # letras=["C","D","F","K","L","N"] 
    # letras=["G","I","J","P","Y","X"] 

    path = os.getcwd().replace("\\","/")+'/chromedriver.exe'#Caminho do ChromeDriver
    options = Options()
    options.add_argument("start-maximized")    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #Caminho para o ChromeDriver    
    
    #DAR NUMERO AO CAMPUS   
    for z in letras:
        try:          
            driver.get(f'http://www4.vestibular.ufjf.br/2022/notaspism2_aposrevisao/{z}.html')
            sleep(0.8) 
            driver.refresh() 
            plusButtons = driver.find_elements(by=By.CLASS_NAME, value='fa-plus')

            for bt in plusButtons:
                 bt.click()
            
            sleep(0.5) 
            quantidade = len(plusButtons)
            if quantidade == 0:
                continue

            # #Criar Listas(vetores) vazios ou completos
            _nomes=[]
            _inscricoes=[]
            _totalPontos=[]
            _port_P1=[]
            _mat_P1=[]
            _lit_P1=[]
            _hist_P1=[]
            _geo_P1=[]
            _fis_P1 =[]
            _qui_P1 =[]
            _bio_P1 =[]
            _port_disc_P1=[]
            _mat_disc_P1=[]
            _lit_disc_P1=[]
            _hist_disc_P1=[]
            _geo_disc_P1=[]
            _fis_disc_P1 =[]
            _qui_disc_P1 =[]
            _bio_disc_P1 =[]
            _port_P2=[]
            _mat_P2=[]
            _lit_P2=[]
            _hist_P2=[]
            _geo_P2=[]
            _fis_P2=[]
            _qui_P2=[]
            _bio_P2=[]
            _port_disc_P2=[]
            _mat_disc_P2=[]
            _lit_disc_P2=[]
            _hist_disc_P2=[]
            _geo_disc_P2=[]
            _fis_disc_P2=[]
            _qui_disc_P2=[]
            _bio_disc_P2=[]

            #Entra nos <tr> com os microdados começando com 2 até quantidade++
            for i in range(2,quantidade*2+1,2): #de 2 em 2   
                nome = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i-1}]/td[2]').text
                print(nome)
                inscricao = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[1]/td').text
                totalPontos = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[2]/td').text
                
                port_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[5]/td[3]').text
                mat_P1= driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[6]/td[3]').text
                lit_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[7]/td[3]').text
                hist_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[8]/td[3]').text
                geo_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[9]/td[3]').text
                fis_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[10]/td[3]').text
                qui_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[11]/td[3]').text
                bio_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[12]/td[3]').text
                port_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[13]/td[3]').text
                mat_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[14]/td[3]').text
                lit_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[15]/td[3]').text
                hist_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[16]/td[3]').text
                geo_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[17]/td[3]').text
                fis_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[18]/td[3]').text
                qui_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[19]/td[3]').text
                bio_disc_P1 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[20]/td[3]').text
                
                port_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[24]/td[3]').text
                mat_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[25]/td[3]').text
                lit_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[26]/td[3]').text
                hist_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[27]/td[3]').text
                geo_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[28]/td[3]').text
                fis_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[29]/td[3]').text
                qui_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[30]/td[3]').text
                bio_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[31]/td[3]').text
                port_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[32]/td[3]').text
                mat_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[33]/td[3]').text
                lit_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[34]/td[3]').text
                hist_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[35]/td[3]').text
                geo_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[36]/td[3]').text
                fis_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[37]/td[3]').text
                qui_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[38]/td[3]').text
                bio_disc_P2 = driver.find_element(by=By.XPATH, value=f'//*[@id="example"]/tbody/tr[{i}]/td/table/tbody/tr[39]/td[3]').text

                
                #Adicionar linha com aluno nos vetores criados
                _nomes.append(nome)
                _inscricoes.append(inscricao.replace('Inscrição: ',''))
                _totalPontos.append(atof(totalPontos.replace('Total Ponderado de Pontos: ','')))
                
                _port_P1.append(atof(port_P1.replace('**','0')))
                _mat_P1.append(atof(mat_P1.replace('**','0')))
                _lit_P1.append(atof(lit_P1.replace('**','0')))
                _hist_P1.append(atof(hist_P1.replace('**','0')))
                _geo_P1.append(atof(geo_P1.replace('**','0')))
                _fis_P1.append(atof(fis_P1.replace('**','0')))
                _qui_P1.append(atof(qui_P1.replace('**','0')))
                _bio_P1.append(atof(bio_P1.replace('**','0')))
                _port_disc_P1.append(atof(port_disc_P1.replace('**','0')))
                _mat_disc_P1.append(atof(mat_disc_P1.replace('**','0')))
                _lit_disc_P1.append(atof(lit_disc_P1.replace('**','0')))
                _hist_disc_P1.append(atof(hist_disc_P1.replace('**','0')))
                _geo_disc_P1.append(atof(geo_disc_P1.replace('**','0')))
                _fis_disc_P1.append(atof(fis_disc_P1.replace('**','0')))
                _qui_disc_P1.append(atof(qui_disc_P1.replace('**','0')))
                _bio_disc_P1.append(atof(bio_disc_P1.replace('**','0')))

                _port_P2.append(atof(port_P2.replace('**','0') ))
                _mat_P2.append(atof(mat_P2.replace('**','0') ))
                _lit_P2.append(atof(lit_P2.replace('**','0') ))
                _hist_P2.append(atof(hist_P2.replace('**','0') ))
                _geo_P2.append(atof(geo_P2.replace('**','0') ))
                _fis_P2.append(atof(fis_P2.replace('**','0') ))
                _qui_P2.append(atof(qui_P2.replace('**','0') ))
                _bio_P2.append(atof(bio_P2.replace('**','0') ))
                _port_disc_P2.append(atof(port_disc_P2.replace('**','0') ))
                _mat_disc_P2.append(atof(mat_disc_P2.replace('**','0') ))
                _lit_disc_P2.append(atof(lit_disc_P2.replace('**','0') ))
                _hist_disc_P2.append(atof(hist_disc_P2.replace('**','0') ))
                _geo_disc_P2.append(atof(geo_disc_P2.replace('**','0') ))
                _fis_disc_P2.append(atof(fis_disc_P2.replace('**','0') ))
                _qui_disc_P2.append(atof(qui_disc_P2.replace('**','0') ))
                _bio_disc_P2.append(atof(bio_disc_P2.replace('**','0') ))

        
            #Juntar listas na transposta
            linhas = list(zip(*[_nomes,_inscricoes,_totalPontos,_port_P1,_mat_P1,_lit_P1,_hist_P1,_geo_P1,_fis_P1,_qui_P1,_bio_P1,_port_disc_P1,_mat_disc_P1,_lit_disc_P1,_hist_disc_P1,_geo_disc_P1,_fis_disc_P1,_qui_disc_P1,_bio_disc_P1,_port_P2,_mat_P2,_lit_P2,_hist_P2,_geo_P2,_fis_P2,_qui_P2,_bio_P2,_port_disc_P2,_mat_disc_P2,_lit_disc_P2,_hist_disc_P2,_geo_disc_P2,_fis_disc_P2,_qui_disc_P2,_bio_disc_P2]))
           
            #Escrever em arquivo CSV
            filename = f'microdados-letra-{z}.csv'
            
            f = open(filename, "w") #Abrir arquivo
            headers = "Nome, Inscricao,Total de pontos, port_P1, mat_P1,lit_P1,hist_P1,geo_P1,fis_P1,qui_P1,bio_P1,port_disc_P1,mat_disc_P1,lit_disc_P1,hist_disc_P1,geo_disc_P1,fis_disc_P1,qui_disc_P1,bio_disc_P1,port_P2, mat_P2,lit_P2,hist_P2,geo_P2,fis_P2,qui_P2,bio_P2,port_disc_P2,mat_disc_P2,lit_disc_P2,hist_disc_P2,geo_disc_P2,fis_disc_P2,qui_disc_P2,bio_disc_P2\n" #Cabeçalho
            f.write(headers) #Escrever Cabeçalho
                
            for i in range(0,quantidade):
                f.write(f'{linhas[i]}\n') #Escrevendo no arquivo csv
                
            f.close() #Fechar arquivo  
            driver.refresh()
            print(filename)


        except Exception as e: #Tratamento de Erro
            print(f'Erro no candidato {nome}')
            print(e)
            driver.refresh()
    
    print(f'FIM da letra {z}!')



if __name__ == '__main__':
    main()