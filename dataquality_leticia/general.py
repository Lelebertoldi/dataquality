import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display


def head(instance):
    texto = f"\n ==*==*==*== Início do Arquivo ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.head()))
    print(texto)
    display(instance.df.head())
    print(f"\n ______________________________________________________________________________ \n")


def tail(instance):
    texto = f"\n ==*==*==*== Final do Arquivo ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.tail()))
    print(texto)
    display(instance.df.tail())
    print(f"\n ______________________________________________________________________________ \n")


def shape(instance):
    texto = f"\n ==*==*==*== Quantidade de Linhas/Colunas ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.shape))
    print(texto)
    display(instance.df.shape)
    print(f"\n ______________________________________________________________________________ \n")


def columns(instance):
    texto = f"\n ==*==*==*== Nome das Colunas ==*==*==*== \n\n"
    colunas_lista = ', '.join(instance.df.columns)
    instance.salvar_texto_pdf(texto + colunas_lista)
    print(texto)
    display(pd.DataFrame(instance.df.columns, columns=['Nomes das Colunas']))
    print(f"\n ______________________________________________________________________________ \n")


def describe(instance):
    texto = f"\n ==*==*==*== Relatório Estatístico Geral ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.describe()))
    print(texto)
    display(instance.df.describe())
    print(f"\n ______________________________________________________________________________ \n")


def duplicated(instance):
    texto = f"\n ==*==*==*== Quantidade de Registros Duplicados ==*==*==*== \n\n {instance.df.duplicated().sum()}"
    instance.salvar_texto_pdf(texto)
    print(texto)
    print(f"\n ______________________________________________________________________________ \n")


# Matriz de calor / correlação das colunas
def heat_matrix(instance):
    # Filtra apenas as colunas numéricas para a correlação
    df_num = instance.df.select_dtypes(include=np.number)
    
    if df_num.empty:
        texto = "Não há colunas numéricas disponíveis no DataFrame."
        instance.salvar_texto_pdf(texto)
        print(texto)
    else:
        # Se houver colunas numéricas cria matriz de correlação
        correlacao = df_num.corr()
        # Se correlação não for vazia mostra correlação
        if not correlacao.empty:
            texto = "\n ==*==*==*== Matriz de Correlação das Colunas Numéricas ==*==*==*== \n\n"
            instance.salvar_texto_pdf(texto + str(correlacao))
            print(texto, correlacao)
            # Define tamanho 
            plt.figure(figsize=(10, 8))
            # Define mapa de calor
            plt.matshow(correlacao, cmap='coolwarm')
            # Define cores
            plt.colorbar()
            # Eixos x e y
            plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=90)
            plt.yticks(range(len(correlacao.columns)), correlacao.columns)
            plt.title("Mapa de calor da matriz de correlação")
            # Ajuste para nada se sobrepor nem fugir da margem
            plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
            # Salva gráfico no PDF
            instance.pdf_pages.savefig(plt.gcf())
            plt.show()
        else:
            texto = "A matriz de correlação está vazia."
            instance.salvar_texto_pdf(texto)
            print(texto)

    print("\n ______________________________________________________________________________ \n")


