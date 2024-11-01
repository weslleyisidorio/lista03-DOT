from random import randint


def criarLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        while True:
            numero = randint(0, 50)
            if numero not in lista:
                lista.append(numero)
                break

    return lista


def separaParImpar(lista):
    par = []
    impar = []
    for elemento in lista:
        if elemento % 2 == 0:
            par.append(elemento)
        else:
            impar.append(elemento)

    return [par, impar]


def main():
    qtdElemetos = 6
    lista = criarLista(qtdElemetos)
    listaSeparada = separaParImpar(lista)

    print("-------------------------------")
    print(f"Lista original: {lista}")
    print(f"Lista separada: {listaSeparada}")


if __name__ == "__main__":
    main()
