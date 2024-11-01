from random import randint


def criarLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        lista.append(randint(0, 10))

    return lista


def ordCont(lista):
    saida = []
    listaOrd = sorted(lista, reverse=True)
    for elemento in listaOrd:
        tupla = (elemento, listaOrd.count(elemento))
        if tupla not in saida:
            saida.append(tupla)

    return saida


def main():
    qtdElemetos = 5
    lista = criarLista(qtdElemetos)
    ordenado = ordCont(lista)

    print("-------------------------------")
    print(f"Lista original: {lista}")
    print(f"Lista ordenada: {ordenado}")


if __name__ == "__main__":
    main()
