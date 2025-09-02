# 1. Abrindo um arquivo inexistente
# Objetivo: Usar try/except para lidar com erro de arquivo não encontrado.
# Enunciado: Tente abrir o arquivo dados.txt e exibir seu conteúdo. Se o arquivo não
# existir, exiba uma mensagem amigável e crie o arquivo com uma mensagem
# padrão.


try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except Exception as e:
    print('Não foi possível abrir o arquivo:', e)

    with open('padrão.txt', 'w') as padrao:
        padrao.write('Arquivo Padrão')