frase = input("Digite uma frase: ").lower()

contador = 0
vogais = "aeiou"

for letra in frase:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)