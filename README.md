# Simulator Twitter Data Extraction

Este projeto consiste em uma simulação da API do Twitter para extração de dados, sem a necessidade de credenciais reais.

## Estrutura do Projeto

O projeto está dividido em três arquivos principais:

1. **twitter_hook.py:** Um hook personalizado para interagir com a simulação da API do Twitter e realizar a busca de tweets com base em uma consulta, período de início e término.

2. **twitter_operator.py:** Um operador personalizado que utiliza o `TwitterHook` para executar a busca de tweets e salvar os resultados em um arquivo JSON.

3. **twitter_dag.py:** Uma DAG (Directed Acyclic Graph) que utiliza o `TwitterOperator` para criar uma pipeline completa de simulação de extração de dados do Twitter. A DAG é programada para ser executada diariamente.

## Uso

Este projeto foi desenvolvido de forma a não requerer credenciais para acesso à API do Twitter. Isso significa que você pode executar a DAG ou o script `twitter_operator.py` sem a necessidade de configurar credenciais da API do Twitter.

### Execução Manual

Você pode executar manualmente a simulação de extração de dados do Twitter utilizando o script `twitter_operator.py`. Certifique-se de fornecer o caminho do arquivo de saída, a consulta desejada e os tempos de início e término.

## DAG Automática
A DAG twitter_dag.py está configurada para ser executada diariamente e utiliza a simulação da API do Twitter, sem a necessidade de fornecer credenciais.

## Requisitos
Python 3.9 - Apache Airflow

## Contribuição
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para criar uma issue ou enviar um pull request.
