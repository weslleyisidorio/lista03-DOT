from random import randint


def criarLista(qtdelementos):
    lista = []
    for i in range(qtdelementos):
        lista.append(randint(-10, 10))

    return lista


def remover_duplicatas(lista):
    listaLimpa = []
    for i in range(len(lista)):
        if lista[i] not in listaLimpa:
            listaLimpa.append(lista[i])

    return listaLimpa


def main():
    qtdElementos = 10
    lista = criarLista(qtdElementos)
    listaLimpa = remover_duplicatas(lista)

    print("-------------------------------")

    print(f"Lista Original: {lista}")
    print(f"Lista sem duplicatas: {listaLimpa}")


if __name__ == "__main__":
    main()
