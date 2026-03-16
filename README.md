# 📊 Desafio de ETL com Python - Santander Dev Week

Este repositório contém a minha solução prática para o desafio de projeto da **Santander Dev Week**, promovida pela DIO. O objetivo principal do projeto é aplicar o conceito de **ETL (Extração, Transformação e Carregamento)** utilizando a linguagem Python.

## 🎯 Objetivo do Projeto

Com base nas aulas do bootcamp, o desafio consistia em consumir dados de clientes, processá-los (gerando mensagens de marketing) e devolvê-los. 

Para garantir que a aplicação rode de forma independente, resiliente e sem depender de instabilidades de APIs externas (como a API da Dev Week ou chaves de IA pagas), optei por desenvolver uma solução local focada na **lógica de programação e manipulação de estruturas de dados (Dicionários e Listas)** em Python.

## ⚙️ O Pipeline ETL Construído

O código foi dividido rigorosamente nas três etapas do processo ETL:

1. **Extract (Extração):** * Simulação da extração de uma base de dados estruturada no formato JSON/Dicionário, contendo informações de contas bancárias de 5 clientes (nome, conta, saldo e limite).

2. **Transform (Transformação):** * Implementação de um algoritmo inteligente que itera (loop `for`) sobre cada cliente. 
   * Utilização de estruturas condicionais (`if/elif/else`) para analisar o saldo de cada um e gerar um "conselho de investimento" ou "aviso financeiro" totalmente personalizado e condizente com a realidade da conta.

3. **Load (Carregamento):** * Inserção dos dados transformados (a nova mensagem) de volta na estrutura de dados do cliente (na lista de `news`).
   * "Carregamento" final simulado através de um relatório limpo e formatado no console para fácil leitura das equipes de negócio.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Lógica de Programação, Estrutura de Dados, Funções e Pipeline ETL.

---
Desenvolvido como portfólio prático de Ciência de Dados e Python 🚀
