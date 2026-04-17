notas = [8.5, 6.0, 7.2, 5.5, 9.0, 4.8, 7.8]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade de notas acima de 7:", contador)