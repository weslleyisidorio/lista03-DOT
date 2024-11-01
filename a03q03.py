from random import randint


def criarLista(qtdelementos):
    """
    lista = []
    for i in range(qtdelementos):
        lista.append(int(input("Digite um número: ")))

    return lista
    """
    lista = []
    for i in range(qtdelementos):
        lista.append(randint(-10, 10))

    return lista


def aoQuadrado(lista):
    saida = []
    for i in range(len(lista)):
        saida.append(pow(lista[i], 2))

    return saida


def main():
    qtdElementos = 10
    lista = criarLista(qtdElementos)
    listaQuadrado = aoQuadrado(lista)

    print("--------------------------")
    print(f"Lista Original: {lista}")
    print(f"Lista ao Quadrado: {listaQuadrado}")


if __name__ == "__main__":
    main()
