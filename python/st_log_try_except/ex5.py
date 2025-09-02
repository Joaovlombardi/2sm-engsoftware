# 5. Copiando arquivos com validação
# Objetivo: Usar try/except para copiar conteúdo de arquivos.
# Enunciado: Solicite o nome de um arquivo para copiar. Copie o conteúdo para
# copia.txt. Trate erros como arquivo não encontrado ou permissão negada.

origem = input("Digite o nome do arquivo que deseja copiar: ")

try:
    with open(origem, "r") as arquivo_origem:
        conteudo = arquivo_origem.read()

    with open("copia.txt", "w") as arquivo_destino:
        arquivo_destino.write(conteudo)

    print("Arquivo copiado com sucesso para 'copia.txt'.")

except FileNotFoundError:
    print(f"[ERRO] O arquivo '{origem}' não foi encontrado.")

except Exception as e:
    print(f"[ERRO] Ocorreu um problema inesperado: {e}")
