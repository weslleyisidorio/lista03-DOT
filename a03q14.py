from random import randint


def criarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(randint(-30, 30))
        matriz.append(linha)
    return matriz


def somarLinhas(matriz):
    somatorios = []
    for linha in matriz:
        somatorio = 0
        for elemntento in linha:
            somatorio += elemntento
        somatorios.append(somatorio)

    return somatorios


def main():
    matriz = criarMatriz(3, 3)
    matrizSomada = somarLinhas(matriz)

    print("-------------------------------")
    print(f"Matriz: {matriz}")
    print(f"Somatório das linhas: {matrizSomada}")


if __name__ == "__main__":
    main()
