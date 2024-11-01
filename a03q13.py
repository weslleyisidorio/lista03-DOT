from random import randint


def sorteio():
    return randint(-100, 100)


def criarLista(qtdelementos):
    lista = []
    for i in range(qtdelementos):
        numero = sorteio()
        while numero in lista:
            numero = sorteio()

        lista.append(numero)

    return lista


def rotacinar_lista(lista, rotacoes):
    copia = lista.copy()
    rotacionada = []
    for i in range(rotacoes):
        rotacionada.insert(0, copia.pop())

    for j in range(len(lista) - rotacoes):
        rotacionada.append(lista[j])

    return rotacionada


def main():
    qtdElementos = 5
    lista = criarLista(qtdElementos)

    rotacoes = 2
    listaRotacionada = rotacinar_lista(lista, rotacoes)

    print("-------------------------------")
    print(f"Lista Original: {lista}")
    print(f"Lista Rotacionada: {listaRotacionada}")


if __name__ == "__main__":
    main()
