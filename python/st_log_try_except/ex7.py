# 7. Criação de log de erros
# Objetivo: Usar arquivos para registrar exceções.
# Enunciado: Crie uma calculadora simples que registra todas as exceções em
# log_erros.txt, incluindo o tipo de erro e horário em que ocorreu.

import datetime

while True:
    try:
        a = int(input("Digite o primeiro número (ou 0 para sair): "))
        if a == 0:
            break
        b = int(input("Digite o segundo número: "))
        op = input("Operação (+, -, *, /): ")

        if op == "+":
            print("Resultado:", a + b)
        elif op == "-":
            print("Resultado:", a - b)
        elif op == "*":
            print("Resultado:", a * b)
        elif op == "/":
            print("Resultado:", a / b)
        else:
            print("Operação inválida.")

    except Exception as e:
        with open("log_erros.txt", "a") as log:
            log.write(str(e) + "\n")
        print("Erro registrado em log_erros.txt")
