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


def menor_maior_diferenca(lista):
    maior = lista[0]
    menor = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento

    diferenca = maior - menor

    return diferenca


def main():
    qtdElemetos = 5
    lista = criarLista(qtdElemetos)
    diferenca = menor_maior_diferenca(lista)

    print("-------------------------------")
    print(f"Lista original: {lista}")
    print(f"Diferença entre o maior e o menor elemento: {diferenca}")
    print("-------------------------------")


if __name__ == "__main__":
    main()
