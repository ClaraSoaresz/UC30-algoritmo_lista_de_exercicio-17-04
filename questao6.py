temperaturas = [30, 28, 27, 29, 31, 26, 28]

soma = 0

for t in temperaturas:
    soma += t

media = soma / len(temperaturas)

print("Temperaturas: ", temperaturas)
print("Média da semana: ", media)