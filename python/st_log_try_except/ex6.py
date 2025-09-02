# 6. Lista de compras com persistência
# Objetivo: Praticar leitura e escrita com exceções.
# Enunciado: Crie um programa que permita adicionar itens a uma lista de compras
# persistente em compras.txt. O programa deve:
# • Ler a lista ao iniciar (se o arquivo existir),
# • Permitir adicionar novos itens,
# • Salvar novamente ao final,
# • Tratar possíveis erros.

# 1. Lê a lista se existir
try:
    with open("compras.txt", "r") as arquivo:
        compras = [linha.strip() for linha in arquivo]
except:
    compras = []

# 2. Adiciona itens
while True:
    item = input("Digite um item (ou 'sair' para encerrar): ")
    if item.lower() == "sair":
        break
    compras.append(item)

# 3. Salva a lista de volta
try:
    with open("compras.txt", "w") as arquivo:
        for item in compras:
            arquivo.write(item + "\n")
except:
    print("Erro ao salvar a lista.")
