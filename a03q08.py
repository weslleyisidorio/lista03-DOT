from random import randint


def criarLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        lista.append(randint(-10, 10))

    return lista


def somaListas(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])

    return lista3


def main():
    qtdElementos = 5
    lista1 = criarLista(qtdElementos)
    lista2 = criarLista(qtdElementos)
    lista3 = somaListas(lista1, lista2)

    print("-------------------------------")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print("-------------------------------")
    print(f"Lista 3: {lista3}")


if __name__ == "__main__":
    main()
