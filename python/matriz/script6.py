texto = 'bom dia, boa tarde, boa noite, boa atitude'

lista = texto.split()
print(lista)

ocorrencias = {}

for palavra in lista:
    if palavra in ocorrencias:
        ocorrencias[palavra]+=1
    else:
        ocorrencias[palavra] = 1

print(ocorrencias)
