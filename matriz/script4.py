def criar_matriz_zeros(m, n):
    # Inicializa uma matriz vazia
    matriz = []

    # Loop para criar m linhas
    for i in range(m):
        linha = [] # Cria uma nova linha vazia
        # Loop para adicionar n zeros na linha
        for j in range(n):
            linha.append(0)
        #Adiciona a linha criada à matriz
        matriz.append(linha)

    return matriz

matriz = criar_matriz_zeros(9, 9)
print(matriz)