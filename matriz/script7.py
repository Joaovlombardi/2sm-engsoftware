def criar_matriz_zeros(m, n):
    matriz = []

    for i in range(m):
        linha = []

        for j in range(n):
            linha.append(0)

        linha [j - i] = 1 # e resultado do número subtraido é a posição do 1
        matriz.append(linha)
        print(matriz)