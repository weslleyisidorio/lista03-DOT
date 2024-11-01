def criarLista(qtdElemtos):
    lista = []
    for i in range(qtdElemtos):
        lista.append(i+1)

    return lista


def somatorioPos(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]

    return soma


def main():
    qtdElemtos = 10
    lista = criarLista(qtdElemtos)
    soma = somatorioPos(lista)
    print(f"A soma dos elementos pares da lista é: {soma}")


if __name__ == '__main__':
    main()
