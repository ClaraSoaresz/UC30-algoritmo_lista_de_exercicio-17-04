vendas = [120, 75, 200, 50, 89, 40]

soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print("Soma dos valores pares:", soma)