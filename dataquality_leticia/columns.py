import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display


# Tipo de coluna
def column_type(instance, coluna):
    tipo = instance.df[coluna].dtype
    texto = f"Tipo: {tipo}"
    instance.salvar_texto_pdf(texto)
    print(texto)


# Quantidade de nulos
def quantity_null(instance, coluna):
    nulos = instance.df[coluna].isnull().sum()
    texto = f"Valores nulos: {nulos}"
    instance.salvar_texto_pdf(texto)
    print(texto)


# Quantidade de únicos
def quantity_unique(instance, coluna):
    quantidade_unicos = instance.df[coluna].nunique()
    texto = f"valores únicos: {quantidade_unicos}"
    instance.salvar_texto_pdf(texto)
    print(texto)


# Percentual total de nulos
def percentage_null(instance, coluna):
    nulos = instance.df[coluna].isnull().sum()
    percentual_nulos = (nulos / len(instance.df)) * 100
    texto = f"Distribuição percentual de valores nulos: {percentual_nulos:.2f}%"
    instance.salvar_texto_pdf(texto)
    print(texto)


# Percentual total de únicos
def percentage_unique(instance, coluna):
    quantidade_unicos = instance.df[coluna].nunique()
    percentual_unicos = (quantidade_unicos / len(instance.df)) * 100
    texto = f"Distribuição percentual dos valores únicos: {percentual_unicos:.2f}%\n"
    instance.salvar_texto_pdf(texto)
    print(texto)            


# Contagem e porcentagem de cada valor único e nulo
def value_counts(instance, coluna):
    nulos = instance.df[coluna].isnull().sum()
    # Verifica se a coluna pode ser um índice (valores únicos e sem nulos)
    if nulos == 0 and instance.df[coluna].is_unique:
        texto = "Possível coluna de índice, todos os valores são únicos."
        instance.salvar_texto_pdf(texto)
        print(texto) 
    else:
        # Valores únicos da coluna (sem considerar possíveis índices)
        texto = f"\nListagem dos valores únicos e quantas vezes aparecem\n"
        unique_count = instance.df[coluna].nunique()
        
        # Verifica se a coluna tem mais de 50 valores únicos
        if unique_count > 50:
            texto += f"A coluna possui mais de 50 valores únicos ({unique_count} no total). Exibindo os 50 mais frequentes:\n"
            # Seleciona os 50 valores mais frequentes
            vc_df = pd.DataFrame(instance.df[coluna].value_counts().nlargest(50))
            instance.salvar_texto_pdf(texto + str(vc_df))
            print(texto)
            display(vc_df) 
        else:
            # Exibe todos os valores únicos se tiver menos de 50
            vc_df = pd.DataFrame(instance.df[coluna].value_counts())
            instance.salvar_texto_pdf(texto + str(vc_df))
            print(texto)
            display(vc_df)                      
            # Calcula a contagem e % de cada valor único e de nulos (se tiver menos de 50)
            contagem = instance.df[coluna].value_counts(dropna=False)               
            percentual = contagem / len(instance.df) * 100
            texto = f"\nDistribuição dos valores por percentual: "
            df_percentual = pd.DataFrame({'Contagem': contagem, 'Percentual (%)': percentual})
            instance.salvar_texto_pdf(texto + df_percentual.to_string())
            print(texto)
            display(df_percentual)


# Estatísticas da coluna para qualquer tipo
def describe_column(instance, coluna):
    texto = f"\nEstatísticas Descritivas\n"
    instance.salvar_texto_pdf(texto + str(instance.df[coluna].describe()))
    print(texto)
    descr_df = instance.df[coluna].describe().to_frame()
    display(descr_df)


# Para colunas numéricas, gera o gráfico de distribuição
def distribution_graph(instance, coluna):
    if pd.api.types.is_numeric_dtype(instance.df[coluna]):
        plt.figure(figsize=(10, 5))
        instance.df[coluna].plot(kind='hist', bins=20, title=f'Distribuição da coluna {coluna}')
        plt.xlabel(coluna)
        # Salvar o gráfico no PDF
        instance.pdf_pages.savefig(plt.gcf())
        plt.show()
        plt.close()


# Gráfico de barras para colunas categóricas
def categorical_graph(instance, coluna):
    if pd.api.types.is_categorical_dtype(instance.df[coluna]) or instance.df[coluna].dtype == object:
        plt.figure(figsize=(10, 5))
        instance.df[coluna].value_counts().plot(kind='bar', title=f'Frequência da coluna {coluna}')
        plt.xlabel(coluna)
        plt.ylabel('Frequência')
        # Salvar o gráfico no PDF
        instance.pdf_pages.savefig(plt.gcf())
        plt.show()
        plt.close()


# Análise de séries temporais (se aplicável)
def groupby_date(instance, coluna):
    if pd.api.types.is_datetime64_any_dtype(instance.df[coluna]):
        texto = f"\nDados agrupados por ano: \n {instance.df[coluna].groupby(instance.df[coluna].dt.year).count()}"
        instance.salvar_texto_pdf(texto)
        print(texto) 
        tendencia_mensal = instance.df[coluna].dt.to_period('M').value_counts().sort_index()
        texto = f"Tendência mensal:\n {tendencia_mensal}"
        instance.salvar_texto_pdf(texto)
        print(texto) 
        # Gráfico de tendência
        instance.df[coluna].groupby(instance.df[coluna].dt.year).count().plot(kind='line', title=f'Tendência temporal da coluna {coluna}')
        # Salvar o gráfico no PDF
        instance.pdf_pages.savefig(plt.gcf())
        plt.show()
        plt.close()