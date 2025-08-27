try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except Exception as e:
    print('Não foi possível abrir o arquivo:', e)

    with open('padrão.txt', 'w') as padrao:
        padrao.write('Arquivo Padrão')

