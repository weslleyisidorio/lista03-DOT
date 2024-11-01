from random import randint


def criarLista(qtdelementos):
    lista = []
    for i in range(qtdelementos):
        elemento = randint(-10, 10)
        if elemento not in lista:
            lista.append(elemento)

    return lista


def existeSoma(lista):
    saida = []
    for elemento in lista:
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if (lista[i] + lista[j] == elemento) and \
                   (lista[i] != lista[j]):
                    print(f"{lista[i]} + {lista[j]} = {elemento}")
                    saida.append(elemento)

    return saida


def main():
    qtdElementos = 10
    lista = criarLista(qtdElementos)
    listaSoma = existeSoma(lista)

    print("--------------------------")
    print(f"Lista Original: {lista}")
    print(f"Lista com soma: {listaSoma}")
    print("--------------------------")


if __name__ == "__main__":
    main()
