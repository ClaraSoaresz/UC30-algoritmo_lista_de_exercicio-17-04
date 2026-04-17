total = 0.0

while True:
    try:
        valor = float(input("Digite o valor do item (0 para encerrar): "))
        if valor == 0:
            break
        total += valor
    except ValueError:
        print("Digite um número válido!")

print("Total da compra: ", total)