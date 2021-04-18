from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
'''
    Este programa entra no site PISM e pega os Resultados:
    Ainda escreve em um arquivo excel as notas desses alunos   
'''
filename = "alunos.csv"
f = open(filename, "w")
headers = "Valor, Quartos, Banheiros, Vagas, Area, BRASIL BROKERS\n"
f.write(headers)

for i in range(1, 8):
    #http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_cursos_6190.html #Governador Valadares
    my_url = f'http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_cursos_3087.html'#Juiz de Fora
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    imoveis = page_soup.find_all("div",{"class":"resultItem row"})

    for imovel in imoveis:
        #cod_imovel = imovel.div.a["data-codigo-imovel"]
        valor = imovel.findAll("span", {"class": "valor"})[0].text
        quartos = imovel.findAll("span", {"class": "numero"})[0].text
        banheiros = imovel.findAll("span", {"class": "numero"})[1].text
        vagas = imovel.findAll("span", {"class": "numero"})[2].text
        #area = imovel.findAll("span", {"class": "numero"})[3].text

        #print(f'{cod_imovel}; {valor}; {quartos}; {banheiros}; {vagas}')
        #f.write(cod_imovel + " , " + valor + " , " + quartos + " , " + banheiros + " , " + vagas + "\n")
        f.write(valor + " , " + quartos + " , " + banheiros + " , " + vagas + "\n")

f.close()





