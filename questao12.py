while True:
    print("\n 1-Soma  2-Subtração  3-Multiplicação  4-Divisão  5-Sair")
    opcao = input("Escolha: ")

    if opcao == "5":
        break

    try:
        numero1 = float(input("Número 1: "))
        numero2 = float(input("Número 2: "))

        if opcao == "1":
            print("Resultado:", numero1 + numero2)
        elif opcao == "2":
            print("Resultado:", numero1 - numero2)
        elif opcao == "3":
            print("Resultado:", numero1 * numero2)
        elif opcao == "4":
            if numero2 != 0:
                print("Resultado:", numero1 / numero2)
            else:
                print("Não pode dividir por zero")
        else:
            print("Opção inválida")

    except:
        print("Digite apenas números!")