

import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
'''    Este programa entra no site PISM e pega os Resultados:
    Ainda escreve em um arquivo excel as notas desses alunos   
'''

class RodarJavaScript():
    def __init__(self, parent=None):
        super().__init__(parent)
        self._results = None
        self.loadFinished.connect(self._on_load_finished)
        self.setUrl(QtCore.QUrl("http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_listagem_3087_457_12.html"))

    @QtCore.pyqtSlot(bool)
    def _on_load_finished(self, ok, elementoJs):
        if ok:
            self.runJavaScript( elementoJs,
                self.results_callback,
            )

    def results_callback(self, value):
        self._results = value
        QtCore.QCoreApplication.quit()

    @property
    def results(self):
        return self._results


if __name__ == "__main__":

    filename = "alunos.csv"
    f = open(filename, "w")
    headers = "Nome, Inscrição, Total de Pontos, Classificação, Situação\n"
    f.write(headers)

    url_grupoA = f'http://www4.vestibular.ufjf.br/2021/resultadofinalpism3/aprovados_listagem_3087_457_12.html' 
    uClient = uReq(url_grupoA)
    page_html = uClient.read()
    uClient.close()
        
    page_soup = soup(page_html, "html.parser")
    aprovados = page_soup.findAll('script')
    # print(aprovados)


    # sys.argv.append("--remote-debugging-port=8000")
    app = QtWidgets.QApplication(sys.argv)
    page = RodarJavaScript(aprovados)
    ret = app.exec_()
    results = page.results
    print(json.dumps(results, indent=4)) 

    f.close()




