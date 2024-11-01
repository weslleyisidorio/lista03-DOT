from random import randint


def criarLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        while True:
            numero = randint(0, 100)
            if numero not in lista:
                lista.append(numero)
                break

    return lista


def criarPares(lista, k):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))

    return pares


def main():
    qtdElemetos = 50
    lista = criarLista(qtdElemetos)
    k = 3
    pares = criarPares(lista, k)

    print("-------------------------------")
    print(f"Lista original: {lista}")
    print(f"Pares que somam {k}: {pares}")
    print("-------------------------------")


if __name__ == "__main__":
    main()
