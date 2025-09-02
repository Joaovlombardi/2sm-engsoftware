# 4. Lendo e escrevendo dados ao mesmo tempo
# Objetivo: Usar try/except para leitura e escrita combinadas.
# Enunciado: Leia um arquivo chamado alunos.txt com linhas no formato: Nome,
# Nota. Para cada aluno com nota abaixo de 6, grave seu nome em reprovados.txt.

try:
    with open("alunos.txt", "r") as entrada, open("reprovados.txt", "w") as saida:
        for linha in entrada:
            try:
                # separa em duas partes: nome e nota
                nome, nota = linha.split(",")

                nota = float(nota)  # converte nota para número, porque veio como texto

                if nota < 6:
                    saida.write(nome + "\n")

            except ValueError:
                print(f"Linha inválida ignorada: {linha.strip()}")

    print("Arquivo 'reprovados.txt' gerado com sucesso!")

except FileNotFoundError:
    print("O arquivo 'alunos.txt' não foi encontrado.")

# strip() = limpa a sujeira no começo e no fim da string.
# split() = quebra a string em pedaços.