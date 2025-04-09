pares = 0
impares = 0
contador = 0

while True:
    numero = int(input(f"Digite o {contador + 1}º numero: "))
    
    if numero == (numero // 2) * 2:
        pares += 1
    else:
        impares += 1
    
    contador += 1
    
    if contador == 10:
        break

print(f"\nQuantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")
