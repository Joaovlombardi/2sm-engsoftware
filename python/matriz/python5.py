def matriz_identidade(m, n):
    matriz = []

    for i in range(m):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

matriz = matriz_identidade(10, 10)
print(matriz)
