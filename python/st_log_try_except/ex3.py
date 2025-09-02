# 3. Gravando nomes em arquivo
# Objetivo: Escrever dados em arquivo com segurança.
# Enunciado: Peça ao usuário nomes até ele digitar "sair". Grave todos os nomes no
# arquivo nomes.txt. Trate qualquer erro de escrita no disco

try:
    with open("nomes.txt", "w") as arquivo: 
        while True:
            nome = input("Digite um nome (ou 'sair' para encerrar): ")

            if nome() == "sair":
                break 

            try:
                arquivo.write(nome + "\n") 
            except:
                print("Não foi possível gravar o nome no arquivo.")

    print("Todos os nomes foram gravados com sucesso!")

except:
    print("Não foi possível abrir ou criar o arquivo 'nomes.txt'.")
