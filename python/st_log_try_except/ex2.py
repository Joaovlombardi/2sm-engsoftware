# 2. Lendo números de um arquivo
# Objetivo: Ler dados de arquivo e tratar erros de conversão.
# Enunciado: O arquivo numeros.txt contém um número por linha. Some todos os
# números. Caso alguma linha não seja um número válido, ignore e continue a
# soma.

soma = 0

try:
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            try:
                soma += int(linha)
            except ValueError:
                print(f"Linha inválida ignorada: {linha}")

    print("Soma total:", soma)

except FileNotFoundError:
    print("O arquivo 'numeros.txt' não foi encontrado.")
