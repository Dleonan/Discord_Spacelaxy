def criar_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"Digite o valor do elemento [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)

    return matriz


def operacao_elemento_matriz(matriz, operacao, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if operacao == 'somar':
                matriz[i][j] += valor
            elif operacao == 'subtrair':
                matriz[i][j] -= valor
            elif operacao == 'multiplicar':
                matriz[i][j] *= valor
            elif operacao == 'dividir':
                if valor != 0:
                    matriz[i][j] /= valor
                else:
                    print("Erro: divisão por zero.")
                    return matriz
    return matriz


def operacao_total_matriz(matriz, operacao, valor):
    soma_total = sum(sum(linha) for linha in matriz)

    if operacao == 'somar':
        return soma_total + valor
    elif operacao == 'subtrair':
        return soma_total - valor
    elif operacao == 'multiplicar':
        return soma_total * valor
    elif operacao == 'dividir':
        if valor != 0:
            return soma_total / valor
        else:
            print("Erro: divisão por zero.")
            return soma_total
    else:
        print("Operação inválida!")
        return soma_total


def menu():
    print("Operações disponíveis:")
    print("1. Criar matriz")
    print("2. Realizar operação em cada elemento da matriz (somar, subtrair, multiplicar, dividir)")
    print("3. Realizar operação com a soma total da matriz (somar, subtrair, multiplicar, dividir)")
    print("0. Sair")


if __name__ == "__main__":
    matriz = None

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            matriz = criar_matriz()
            print("Matriz criada:")
            for linha in matriz:
                print(linha)

        elif opcao == "2":
            if matriz is None:
                print("Você deve criar uma matriz primeiro.")
            else:
                operacao = input("Escolha a operação (somar, subtrair, multiplicar, dividir): ")
                valor = float(input("Digite o valor para a operação: "))
                matriz = operacao_elemento_matriz(matriz, operacao, valor)
                print("Matriz após a operação:")
                for linha in matriz:
                    print(linha)

        elif opcao == "3":
            if matriz is None:
                print("Você deve criar uma matriz primeiro.")
            else:
                operacao = input("Escolha a operação (somar, subtrair, multiplicar, dividir): ")
                valor = float(input("Digite o valor para a operação: "))
                resultado = operacao_total_matriz(matriz, operacao, valor)
                print(f"Resultado da operação com a soma total da matriz: {resultado}")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
