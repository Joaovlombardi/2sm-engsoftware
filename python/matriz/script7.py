def criar_matriz_zeros(m, n):
    matriz = []

    for i in range(m):
        linha = []

        for j in range(n):
            linha.append(0)

        linha [j - i] = 1
        matriz.append(linha)
    return matriz

matriz = criar_matriz_zeros(5, 5)
for linha in matriz:
    print(linha)
