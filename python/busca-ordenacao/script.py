# numero = 10
# lista = [1, 7, 9, 10]
#
#
# try:
#     print(lista[2])
#
# except ZeroDivisionError as e: #Posso ter mais de um except
#     print('Não posso dividir por zero: ', e)
#
# except Exception as ex:
#     print("Deu erro:", ex)
#
# finally: #Encerra
#     print("Encerrando...")

#------------------------------

# import os #biblioteca para criar diretorios
#
# directory_name = "my_new_directory"
# os.mkdir(directory_name)
#
# with open(f'{directory_name}/exemplo.py', 'w') as arquivo:
#     print('Arquivo Criado!')

#------------------------------

# import os
#
# caminho_arquivo = 'exemplo.txt'
# # Verificar se o arquivo existe antes de tentar excluí-lo
# if os.path.exists(caminho_arquivo):
#     os.remove(caminho_arquivo)
#     print(f'O arquivo {caminho_arquivo} foi excluído.')
# else:
#     print(f'O arquivo {caminho_arquivo} não existe.')

#------------------------------

import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG,
format='%(asctime)s - %(levelname)s - %(message)s')

try:
    print(10/0)
except Exception as e:
    logging.error(f'Ocorreu um erro inesperado: {e}')
