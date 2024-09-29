import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import shutil
from IPython.display import display, Markdown
from .general import *  
from .columns import * 


class RelatorioCSV:
    def __init__(self, caminho_arquivo):
        # Lê o arquivo CSV e armazena o DataFrame
        self.df = pd.read_csv(caminho_arquivo)
        self.pdf_pages = PdfPages('relatorio_CSV.pdf') # Adiciona imagens/gráficos ao PDF como páginas


    # Salva os textos no pdf como imagens
    def salvar_texto_pdf(self, texto):
        plt.figure()
        plt.text(0.5, 0.5, texto, ha='center', va='center', fontsize=12)
        plt.axis('off')  # Não exibe eixos
        self.pdf_pages.savefig(plt.gcf())  # Salva a figura no PDF
        plt.close()  # Fecha a figura  


    # Chama os métodos no arquivo general.py
    def geral(self):
        head(self)
        sample(self)
        tail(self)
        shape(self)
        columns(self)
        describe(self)
        duplicated(self)
        missing_values(self)
        heat_matrix(self)
        print(f"\n ____________________________________________________________________________________________________________________________________________ \n")
        print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


    # Chama os métodos no arquivo columns.py e itera eles sobre cada coluna do DataFrame
    def colunas(self):
        for coluna in self.df.columns:
            display(Markdown(f"## Relatório da Coluna: {coluna}"))
            texto = f"\nRelatório da Coluna: {coluna}\n\n "
            self.salvar_texto_pdf(texto)
            column_type(self, coluna)
            quantity_null(self, coluna)
            quantity_unique(self, coluna)
            percentage_null(self, coluna)
            percentage_unique(self, coluna)
            value_counts(self, coluna)
            describe_column(self, coluna)
            distribution_graph(self, coluna)
            categorical_graph(self, coluna)
            groupby_date(self, coluna)
            print(f"\n ____________________________________________________________________________________________________________________________________________ \n")
            print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


    def fechar_pdf(self):
        self.pdf_pages.close()


    def relatorio_completo(self):
        self.geral()
        self.colunas()
        self.fechar_pdf()


    def relatotio_geral(self):
        self.geral()
        self.fechar_pdf()


    def relatorio_colunas(self):
        self.colunas()
        self.fechar_pdf()


    def exportar_relatorio(self):
        # Pergunta ao usuário onde salvar o arquivo
        caminho_diretorio = input("Digite o caminho completo para salvar o relatório: ")
        nome_arquivo = "relatorio_CSV.pdf"
        # Combina o caminho do diretório com o nome do arquivo
        caminho_arquivo = f"{caminho_diretorio}/{nome_arquivo}"     
        # Move o PDF gerado para o local especificado
        try:
            shutil.move('relatorio_CSV.pdf', caminho_arquivo)
            print(f"Relatório exportado para {caminho_arquivo}.")
        except PermissionError as e:
            print(f"Erro ao mover o arquivo: {e}")

