# 📊 Análise de Devoluções no Varejo

## 🎯 Objetivo

Este projeto tem como objetivo analisar o impacto financeiro das devoluções em um dataset de vendas de varejo, identificando padrões, produtos problemáticos e oportunidades de melhoria no negócio.

---

## 🧠 Problema de Negócio

Devoluções podem representar um grande prejuízo financeiro e indicar problemas como:

* Produtos defeituosos
* Erros logísticos
* Expectativa vs realidade do cliente

A análise busca responder:

* Qual o impacto financeiro das devoluções?
* Quais produtos possuem maior taxa de devolução?
* Existem padrões por tempo ou região?
* Onde devemos priorizar ações?

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Power BI
* Git & GitHub

---

## 🔧 Tratamento de Dados

* Conversão de datas (`InvoiceDate`)
* Criação da variável `Revenue`
* Separação entre:

  * Vendas (`Quantity > 0`)
  * Devoluções (`Quantity < 0`)
* Identificação de:

  * Dados faltantes
  * Datas inválidas (mais de 300 mil linhas)
* Separação de dados problemáticos para análise futura

---

## 📊 Principais Métricas

* Receita total de vendas
* Receita perdida com devoluções
* Taxa de devolução (%)
* Impacto financeiro das devoluções
* Taxa de devolução por produto
* Taxa de devolução por país
* Taxa de devolução ao longo do tempo

---

## 🔍 Principais Insights

* Aproximadamente **24% das vendas são impactadas por devoluções**
* Alguns produtos apresentam taxas superiores a **100%**, indicando possíveis erros ou problemas críticos
* Meses como **Dezembro e Janeiro** concentram maior volume de devoluções
* Certos países apresentam **alta taxa percentual**, mas baixo impacto financeiro

---

## ⚠️ Qualidade dos Dados

* Mais de **300 mil registros com datas inválidas**
* Aproximadamente **14 mil pedidos afetados**
* Estratégia adotada:

  * Separação dos dados problemáticos
  * Análise principal baseada em dados confiáveis

---

## 📈 Dashboard

O dashboard foi desenvolvido no Power BI e inclui:

* KPIs principais
* Análise temporal
* Produtos críticos
* Análise geográfica

📌 Arquivo disponível em: `dashboard/dashboard.pbix`

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```
git clone https://github.com/Lessa49.git
```

2. Instale as dependências:

```
pip install pandas
```

3. Execute o script:

```
python src/analise.py
```

---

## 💡 Aprendizados

* Estruturação de projetos de dados
* Limpeza e validação de dados
* Análise exploratória com foco em negócio
* Construção de métricas relevantes
* Criação de dashboards no Power BI

---

