import util

def calcular_media_idade(dados):
    total_idade = 0
    for cliente in dados:
        total_idade += int(cliente[2])  
    return total_idade / len(dados)

def calcular_media_renda(dados):
    total_renda = 0
    for cliente in dados:
        total_renda += float(cliente[3])  
    return total_renda / len(dados)


dados_clientes = util.ler_dados_arquivo('clientes.txt')


if dados_clientes:
    media_idade = calcular_media_idade(dados_clientes)
    media_renda = calcular_media_renda(dados_clientes)
    print(f'Média de idade dos clientes: {media_idade:.2f} anos')
    print(f'Média de renda mensal dos clientes: R$ {media_renda:.2f}')
else:
    print("Nenhum dado válido foi encontrado no arquivo.")
