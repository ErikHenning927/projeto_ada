# Documentação da Aplicação Python

Esta documentação fornece uma visão geral do código e da estrutura da aplicação Python composta pelos arquivos `front.py`, `gerar.py` e `main.py`. O objetivo é explicar as principais funcionalidades, módulos utilizados e fornecer informações sobre como executar e contribuir para o projeto.

## Estrutura do Projeto

```
meu_projeto/
|-- front.py
|-- gerar.py
|-- main.py
```

### front.py

O arquivo `front.py` serve como uma interface de linha de comando (CLI) para interação com as funcionalidades principais da aplicação. Ele importa o módulo `main` e o módulo `gerar` para criar registros aleatórios.

A função `main_menu` é responsável por exibir o menu principal da aplicação, permitindo que o usuário escolha diversas opções, como adicionar novo registro, ler registros, atualizar rendimentos, exportar relatórios, entre outras.

### gerar.py

O arquivo `gerar.py` contém funções para gerar registros aleatórios. Utiliza a biblioteca `Faker` para criar dados fictícios, como datas, e a função `gerar_registros_aleatorios` para criar registros aleatórios de receitas, despesas e investimentos.

### main.py

O arquivo `main.py` é o núcleo da aplicação, responsável por manter uma lista de registros, gerenciar rendimentos de investimentos e oferecer funcionalidades como criar, ler, atualizar, deletar registros, além de exportar relatórios em formatos JSON e CSV.

## Funcionalidades Principais

1. **Adicionar Novo Registro:**
   - Solicita informações como tipo (receita, despesa ou investimento), valor e data.
   - Utiliza a função `criar_registro` do módulo `main` para adicionar um novo registro à lista.

2. **Ler Registros:**
   - Utiliza a função `ler_registros` do módulo `main` para exibir todos os registros existentes.

3. **Atualizar Rendimentos:**
   - Utiliza a função `atualizar_rendimentos` do módulo `main` para calcular e atualizar os rendimentos dos investimentos.

4. **Exportar Relatório:**
   - Permite exportar o conjunto atual de registros e rendimentos em formato JSON ou CSV.
   - Utiliza a função `exportar_relatorio` do módulo `main` para realizar a exportação.

5. **Consultar por Data, Tipo e Valor:**
   - Oferece opções para consultar registros com base na data, tipo e valor.
   - Utiliza as funções `consultar_por_data`, `consultar_por_tipo` e `consultar_por_valor` do módulo `main`.

6. **Deletar Registro:**
   - Permite deletar um registro específico com base no ID informado pelo usuário.
   - Utiliza a função `deletar_registro` do módulo `main` para realizar a exclusão.

## Como Executar a Aplicação

Para executar a aplicação, basta rodar o arquivo `front.py`. Certifique-se de ter todas as dependências instaladas. Você pode instalar as dependências executando o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

Em seguida, execute o arquivo `front.py`:

```bash
python front.py
```

Siga as instruções exibidas no terminal para interagir com a aplicação.

## Testes (Comentados)

Existem testes comentados no final do arquivo `main.py` que podem ser descomentados e executados para verificar o funcionamento das principais funcionalidades da aplicação. Certifique-se de ajustar as datas e valores conforme necessário.
