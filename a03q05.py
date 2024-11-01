def maior(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


def main():
    numeros = [3, 6, 9, 12, 15, 18]
    maiorNumero = maior(numeros)
    print(f"O maior número  da lista {numeros} é: {maiorNumero}")


if __name__ == "__main__":
    main()
