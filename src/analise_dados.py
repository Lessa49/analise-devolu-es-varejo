# Métrica principal analisada - impacto financeiro das devoluções

import pandas as pd

# Conversão para DataFrame

df = pd.read_csv('../data/data.csv', encoding='latin1')

# Tratamento de dados

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    dayfirst=True,
    errors="coerce"
)
df['CustomerID'] = df['CustomerID'].astype('Int64').astype('category')
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Qualidade dos dados

#após printar as linhas abaixo identificamos que existem mais de 300 mil linhas com problemas na data, o que prejudica a análise
linhas_totais = len(df)
linhas_sem_data = df['InvoiceDate'].isna().sum()
pedidos_sem_data = df[df['InvoiceDate'].isna()]['InvoiceNo'].nunique()

## Separação dos dados

#vamos dividir a análise em cima da tabela que inclui e a que não inclui os dados com data inválida, para comparar os resultados e entender o impacto desses dados na análise geral
df_data_invalida = df[df['InvoiceDate'].isna()]
df = df.dropna(subset=['InvoiceDate'])

#o código abaixo é uma tentativa de recuperar as datas desses pedidos, usando a data do primeiro pedido válido para cada número de pedido, porém não deu certo
#mapa_datas = datas_validas.groupby('InvoiceNo')['InvoiceDate'].first()
#df['InvoiceDate'] = df['InvoiceDate'].fillna(df['InvoiceNo'].map(mapa_datas))

#vamos analisar a tabela sem os dados com data inválida. Porém também criamos um arquivo com os dados brutos separado
df_data_invalida.to_csv('../data/dados_problematicos.csv', index=False)

## Criação subtabelas

vendas = df[df['Quantity'] > 0].copy()
devolucoes = df[df['Quantity'] < 0].copy()

## Métricas Gerais

receita_vendas = vendas["Revenue"].sum()
receita_devolucoes = devolucoes["Revenue"].sum()

impacto_percentual = (
    abs(receita_devolucoes) / receita_vendas
) * 100
taxa_devolucao_pedidos = (
    devolucoes['InvoiceNo'].nunique() /
    vendas['InvoiceNo'].nunique()
) * 100

# Análise por produto

receita_vendida_prod = vendas.groupby('StockCode')['Revenue'].sum()
receita_devolvida_prod = devolucoes.groupby('StockCode')['Revenue'].sum().abs()

tabela_produto = pd.concat(
    [receita_vendida_prod, receita_devolvida_prod], axis=1
)
tabela_produto.columns = ["receita_vendida", "receita_devolvida"]
tabela_produto = tabela_produto.fillna(0)

tabela_produto['taxa_devolucao_%'] = (
    tabela_produto['receita_devolvida'] /
    tabela_produto['receita_vendida']
) * 100

# Filtro relevante

tabela_produto_filtrada = tabela_produto[
    (tabela_produto["receita_vendida"] > 10000) &
    (tabela_produto["taxa_devolucao_%"] > 20)
]

# Análise temporal - Dezembro e Janeiro são meses críticos para devoluções

vendas["Month"] = vendas["InvoiceDate"].dt.to_period("M")
devolucoes["Month"] = devolucoes["InvoiceDate"].dt.to_period("M")

vendas_por_mes = vendas.groupby("Month")["Revenue"].sum()
devolucoes_por_mes = devolucoes.groupby("Month")["Revenue"].sum().abs()

taxa_mensal = (
    devolucoes_por_mes
    .div(vendas_por_mes, fill_value=0)
    * 100
)

# Análise por país - Singapura, EUA, Hong Kong e Barein são os países com mais devoluções, sendo os dois primeiros 57% e 51%

vendas_por_pais = vendas.groupby('Country')['Revenue'].sum()
devolucoes_por_pais = devolucoes.groupby('Country')['Revenue'].sum().abs()

tabela_pais = pd.concat(
    [vendas_por_pais, devolucoes_por_pais],
    axis=1
)

tabela_pais.columns = ["receita_vendida", "receita_devolvida"]
tabela_pais = tabela_pais.fillna(0)

tabela_pais["taxa_devolucao_%"] = (
    tabela_pais["receita_devolvida"] /
    tabela_pais["receita_vendida"]
) * 100


# Comparação impacto financeiro por país

tabela_pais["impacto_absoluto"] = tabela_pais["receita_devolvida"]

tabela_pais_ordenada = tabela_pais.sort_values(
    by="impacto_absoluto",
    ascending=False
)

df.to_csv('../data/dataset_tratado.csv', index=False, encoding='utf-8')