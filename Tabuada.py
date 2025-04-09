numero = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1