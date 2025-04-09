while True:
    nota = float(input("Digite a nota do aluno (< 7): "))
    if nota > 7:
        print("Nota valida")
        break
    else:
        print("Nota invalida, tente novamente")
