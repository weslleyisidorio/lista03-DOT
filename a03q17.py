from random import randint


def gerarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(randint(0, 10))

        matriz.append(linha)

    return matriz


def traspoeMatriz(matriz):
    matrizT = []
    for i in range(len(matriz[0])):  # colunas
        linha = []
        for j in range(len(matriz)):  # linhas
            linha.append(matriz[j][i])

        matrizT.append(linha)

    return matrizT


def main():
    linhas = 2
    colunas = 3
    matriz = gerarMatriz(linhas, colunas)
    matrizT = traspoeMatriz(matriz)

    print("-------------------------------")
    print(f"Matriz original: {matriz}")
    print(f"Matriz transposta: {matrizT}")
    print("-------------------------------")


if __name__ == "__main__":
    main()
