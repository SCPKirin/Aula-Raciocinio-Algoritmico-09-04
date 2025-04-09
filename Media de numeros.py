soma = 0
contador = 0

while True:
    numero = float(input("Digite um numero (ou -1 para sair): "))
    if numero == -1:
        break
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"Media dos numeros digitados: {media}")
else:
    print("Nenhum numero valido foi digitado")
