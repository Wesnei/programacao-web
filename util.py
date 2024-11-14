def ler_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()
    
    dados = []
    for linha in linhas:
        linha = linha.strip()  
        if linha:  
            cliente = linha.split(';') 
            dados.append(cliente)
    return dados
