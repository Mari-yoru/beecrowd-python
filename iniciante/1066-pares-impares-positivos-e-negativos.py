positivos = 0
pares = 0
impares = 0
negativo = 0

for _ in range(5):
    valor = int(input())

    if valor % 2 == 0:
        pares += 1
    if valor % 2 != 0:
        impares += 1
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativo += 1
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")