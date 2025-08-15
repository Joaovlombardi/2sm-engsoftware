candidatos = [{
    "CandidatoA": 0,
    "CandidatoB": 0,
    "CandidatoC": 0
}]

def menu():
    print('Candidatos para a vaga:\n')
    print('1 - Candidato A')
    print('2 - Candidato B')
    print('3 - Candidato C')

while True:
    menu()
    voto = input("\nDigite o seu voto: ")

    if voto == "1":
        candidatos[0]["CandidatoA"] += 1
    elif voto == "2":
        candidatos[0]["CandidatoB"] += 1
    elif voto == "3":
        candidatos[0]["CandidatoC"] += 1
    elif voto == "fim":
        break
    else:
        print("Digite um número correto...")

print("\nResultado final da votação:")
for candidato, votos in candidatos[0].items():
    print(f"{candidato}: {votos} votos")
