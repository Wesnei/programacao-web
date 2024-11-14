
# Análise de Dados de Clientes

Este repositório contém um simples sistema em Python para calcular a **média de idade** e a **média de renda** de clientes a partir de um arquivo de texto. O programa lê os dados dos clientes, processa as informações e retorna as médias desejadas.

## Arquivos do Repositório

- **`cliente.py`**: Script principal que calcula a média de idade e renda dos clientes.
- **`util.py`**: Contém funções auxiliares, como a leitura dos dados de um arquivo de texto.
- **`clientes.txt`**: Arquivo de entrada com os dados dos clientes. Cada linha contém o nome, cidade, idade e renda de um cliente, separados por ponto e vírgula.

## Estrutura do Repositório

```
analise-clientes/
│
├── cliente.py        # Script principal que calcula as médias
├── util.py           # Funções auxiliares (leitura de arquivo)
├── clientes.txt      # Arquivo de dados dos clientes
└── README.md         # Documentação do projeto
```

## Descrição

O projeto é composto por três arquivos principais:

1. **`clientes.txt`**: Contém informações sobre clientes. Cada linha possui os seguintes campos:
   - Nome do cliente
   - Cidade
   - Idade
   - Renda mensal

   Exemplo do arquivo `clientes.txt`:

   ```
   João; Natal; 25; 3500
   Arthur; Fortaleza; 32; 4200
   Miguel; Recife; 28; 2900
   Maria; São Paulo; 41; 5000
   ```

2. **`util.py`**: Este arquivo contém a função `ler_dados_arquivo(nome_arquivo)`, que lê o arquivo de texto `clientes.txt` e extrai os dados dos clientes. A função retorna uma lista de listas, onde cada sublista representa um cliente e seus dados.

3. **`cliente.py`**: Este script utiliza a função do arquivo `util.py` para ler os dados de clientes e calcular as médias de idade e renda de todos os clientes presentes no arquivo. Ele exibe as médias no terminal.

## Como Usar

### Passo 1: Preparar o ambiente

Certifique-se de que você tenha o Python instalado em sua máquina. O código foi testado com Python 3.6+.

### Passo 2: Adicionar Dados ao Arquivo

Abra o arquivo `clientes.txt` e adicione os dados dos clientes no formato abaixo:

```
Nome; Cidade; Idade; Renda
```

### Passo 3: Executar o Script

Para rodar o programa e calcular as médias de idade e renda dos clientes, basta executar o script `cliente.py`:

```bash
python cliente.py
```

### Saída Esperada

Se os dados forem válidos, o script exibirá a média de idade e a média de renda dos clientes. Por exemplo:

```
Média de idade dos clientes: 31.50 anos
Média de renda mensal dos clientes: R$ 3650.00
```

Se não houver dados válidos ou o arquivo estiver vazio, a seguinte mensagem será exibida:

```
Nenhum dado válido foi encontrado no arquivo.
```

## Funcionalidade

- **`ler_dados_arquivo(nome_arquivo)`**: Lê o arquivo de texto `clientes.txt` e retorna uma lista de clientes, onde cada cliente é representado por uma lista com os valores nome, cidade, idade e renda.
  
- **`calcular_media_idade(dados)`**: Calcula a média das idades de todos os clientes.
  
- **`calcular_media_renda(dados)`**: Calcula a média da renda mensal de todos os clientes.

## Como Funciona o Código

1. **Leitura do Arquivo**: O arquivo `clientes.txt` é lido pela função `ler_dados_arquivo` do arquivo `util.py`. Essa função retorna uma lista de listas, onde cada sublista contém as informações de um cliente.
   
2. **Cálculo das Médias**: O script `cliente.py` usa os dados retornados para calcular a média da idade e a média da renda dos clientes. As funções `calcular_media_idade` e `calcular_media_renda` realizam esse cálculo iterando sobre os dados.

3. **Exibição dos Resultados**: O script imprime no terminal a média de idade e a média de renda dos clientes.

## Contribuindo

Se você gostaria de sugerir melhorias ou correções, fique à vontade para abrir um **Pull Request**. Se encontrar algum erro ou tiver dúvidas, crie uma **Issue** para que possamos ajudar!

## Licença

Este repositório está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
