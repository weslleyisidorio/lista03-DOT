def maior(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


def menor(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor


def main():
    notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]
    maiorNota = maior(notas)
    menorNota = menor(notas)
    print(f"A maior nota da lista {notas} é: {maiorNota}")
    print(f"A menor nota da lista é: {menorNota}")


if __name__ == "__main__":
    main()
