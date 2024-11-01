from random import randint


def criarLista(qtdElementos):
    idades = []
    for i in range(qtdElementos):
        idades.append(randint(0, 100))

    return idades


def maiorIdade(lista):
    listaMaior = [lista[i] for i in range(len(lista)) if lista[i] >= 18]

    return listaMaior


def menorIdade(lista):
    listaMenor = [lista[i] for i in range(len(lista)) if lista[i] < 18]

    return listaMenor


def main():
    qtdElementos = 10
    idades = criarLista(qtdElementos)
    idadesMaior = maiorIdade(idades)
    idadesMenor = menorIdade(idades)

    print("-----------------------------------")
    print(f"Lista Original: {idades}")
    print(f"Lista Maiores de idade: {idadesMaior}")
    print(f"Lista Menor de idade: {idadesMenor}")


if __name__ == "__main__":
    main()
