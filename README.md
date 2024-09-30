# Dataquality para análise de CSV

---

### Dataquality para análise de arquivos CSV

### Modo de uso:

```

from dataquality_leticia.dataquality import RelatorioCSV

# Substitua Forbes_Richest_Atheletes_1990_2020 pelo nome do seu arquivo, se estiver em outra pasta especifique o caminho
relatorio = RelatorioCSV('Forbes_Richest_Atheletes_1990_2020.csv')

# Para análise completa (análise geral + análise coluna por coluna)
relatorio.relatorio_completo()

# Para análise geral (sem análise coluna por coluna)
relatorio.relatotio_geral()

# Para análise coluna por coluna (sem análise geral)
relatorio.relatorio_colunas()

# Para salvar última análise feita em um arquivo PDF, necessário informar caminho onde arquivo será salvo no input
relatorio.exportar_relatorio()

```

--- 

## Conteúdo da análise geral:

- Início do Arquivo (5 primeiras linhas)
- Meio do Arquivo (5 linhas aleatórias)
- Final do Arquivo (5 últimas linhas)
- Quantidade de Linhas/Colunas
- Nomes das Colunas	e seus Tipo de dados
- Relatório Estatístico Geral
- Quantidade de Registros Duplicados
- Valores Faltantes com Gráfico
- Matriz de Correlação das Colunas Numéricas com Gráfico

---

## Conteúdo da análise coluna por coluna:

- Tipo de dados
- Quantidade de Valores Nulos
- Quantidade de Valores Únicos
- Distribuição Percentual de Valores Nulos
- Distribuição Percentual dos Valores Únicos
- Se é Possivel Coluna de Índice (todos os valores são únicos)
- Listagem dos Valores Únicos e Quantas Vezes Aparecem (Apenas para coluna que não seja possível Índice, se tiver mais de 50 valores únicos mostra os 50 mais frequentes)
- Distribuição dos Valores por Percentual (Apenas para coluna que não seja possível Índice e tenha menos de 50 valores únicos)
- Estatísticas Descritivas
- Gráfico de Frequência da Coluna (Para colunas categóricas)
- Gráfico de Distribuição da Coluna (Para colunas numéricas)
- Análise de Séries Temporais com Dados Agrupados por Ano com Tendência Mensal e Gráfico de Tendência Temporal (Para colunas de data)

---

> [!IMPORTANT]
>- **Configurações do Arquivo PDF Ainda Precisam de Ajustes, Algumas Páginas Estão Sendo Cortadas**
>


