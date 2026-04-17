def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return imc, "Abaixo do peso"
    elif imc <= 24.9:
        return imc, "Normal"
    else:
        return imc, "Acima do peso"

try:
    paciente = {}

    paciente["nome"] = input("Qual o seu nome: ")
    paciente["idade"] = int(input("Quantos anos você tem: "))
    paciente["peso"] = float(input("Digite seu peso (kg): "))
    paciente["altura"] = float(input("Digite sua altura (m): "))

    imc, categoria = calcular_imc(paciente["peso"], paciente["altura"])

    print("\nDados")
    print("Nome:", paciente["nome"])
    print("Idade:", paciente["idade"])
    print("Peso:", paciente["peso"])
    print("Altura:", paciente["altura"])
    print("IMC:", round(imc, 2))
    print("Classificação:", categoria)

except ValueError:
    print("Entrada inválida! Digite apenas números para idade, peso e altura.")