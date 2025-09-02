# 8. Desafio: Estatísticas de um arquivo
# Objetivo: Consolidar leitura, escrita e tratamento de erros.
# Enunciado: O arquivo valores.txt contém números separados por vírgula em cada
# linha. Calcule:
# • A média geral de todos os números,
# • O total de números inválidos (não numéricos),
# • Grave um relatório em relatorio.txt.

valores = []
invalidos = 0

try:
    with open("valores.txt", "r") as arquivo:
        for linha in arquivo:
            for item in linha.split(","):
                item = item.strip()
                try:
                    valores.append(float(item))
                except:
                    invalidos += 1

    media = sum(valores) / len(valores) if valores else 0

    with open("relatorio.txt", "w") as rel:
        rel.write(f"Média: {media}\n")
        rel.write(f"Inválidos: {invalidos}\n")

except:
    print("Erro ao processar o arquivo.")
