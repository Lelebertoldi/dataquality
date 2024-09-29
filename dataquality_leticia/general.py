import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from IPython.display import display, Markdown


def head(instance):
    texto = f"\n ==*==*==*== Início do Arquivo ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.head()))
    display(Markdown("## Início do Arquivo"))
    display(instance.df.head())
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def sample(instance):
    texto = f"\n ==*==*==*== Meio do Arquivo ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.sample(5)))
    display(Markdown("## Meio do Arquivo"))
    display(instance.df.sample(5))
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def tail(instance):
    texto = f"\n ==*==*==*== Final do Arquivo ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.tail()))
    display(Markdown("## Final do Arquivo"))
    display(instance.df.tail())
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def shape(instance):
    texto = f"\n ==*==*==*== Quantidade de Linhas/Colunas ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.shape))
    display(Markdown("## Quantidade de Linhas/Colunas"))
    display(instance.df.shape)
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def columns(instance):
    texto = f"\n ==*==*==*== Nome das Colunas ==*==*==*== \n\n"
    df_colunas = pd.DataFrame({
        'Nomes das Colunas': instance.df.columns,
        'Tipo de dados': instance.df.dtypes.astype(str)}).reset_index(drop=True)
    instance.salvar_texto_pdf(texto + df_colunas)
    display(Markdown("## Colunas"))
    display(df_colunas)
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def describe(instance):
    texto = f"\n ==*==*==*== Relatório Estatístico Geral ==*==*==*== \n\n"
    instance.salvar_texto_pdf(texto + str(instance.df.describe()))
    display(Markdown("## Relatório Estatístico Geral"))
    display(instance.df.describe())
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def duplicated(instance):
    texto = f"\n ==*==*==*== Quantidade de Registros Duplicados ==*==*==*== \n\n", instance.df.duplicated().sum()
    instance.salvar_texto_pdf(texto)
    display(Markdown("## Quantidade de Registros Duplicados"))
    display(instance.df.duplicated().sum())
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


def missing_values(instance):
    # Calcular a contagem de nulos e a porcentagem de nulos
    null_counts = instance.df.isnull().sum()
    total_rows = len(instance.df)
    null_percentages = (null_counts / total_rows) * 100   
    # Criar um DataFrame com os resultados
    missing_values_df = pd.DataFrame({
        'Nome da Coluna': null_counts.index,
        'Contagem de Nulos': null_counts.values,
        'Porcentagem de Nulos': null_percentages.round(2).astype(str) + '%'})
    # Filtrar para apenas colunas com valores nulos
    missing_values_df = missing_values_df[missing_values_df['Contagem de Nulos'] > 0]    
    # Exibir o relatório
    display(Markdown("## Valores Faltantes"))
    display(missing_values_df)
    print("\n")  
    # Exibir gráfico se houver valores faltantes
    if not missing_values_df.empty:
        plt.figure(figsize=(10, 6))
        plt.bar(missing_values_df['Nome da Coluna'], missing_values_df['Contagem de Nulos'], color='cornflowerblue')
        plt.xticks(rotation=45)
        plt.title('Contagem de Valores Faltantes')
        plt.xlabel('Nome da coluna')
        plt.ylabel('Contagem de Nulos')
        plt.tight_layout()
        plt.show()
    else:
        print("Não há valores faltantes no DataFrame.")
    print(f"\n ____________________________________________________________________________________________________________________________________________ \n")


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
            display(Markdown("## Matriz de Correlação das Colunas Numéricas"))
            display(correlacao)
            print('\n')
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



