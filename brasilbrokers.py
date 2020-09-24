from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
'''
Este programa entra no site BRASIL BROKERS e pega os 15 (ou menos) imóveis com os seguintes filtros:
    Local: Jardim Guanabara - RJ
    Preço: R$300.000,00 - R$500.000,00
    Ordem: Crescente de preço
    Quartos: 1+
Ainda escreve em um arquivo excel os dados destes imóveis    
'''
filename = "imoveis.csv"
f = open(filename, "w")
headers = "Valor, Quartos, Banheiros, Vagas, Area, BRASIL BROKERS\n"
f.write(headers)

for i in range(1, 8):
    my_url = f'https://brasilbrokers.com.br/busca/?mercado=pronto&localizacao=jardim-guanabara|rio-de-janeiro|rj&dormitorio=1&preco=300000,900000&pagina={i}&ordem=menor-preco'
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





