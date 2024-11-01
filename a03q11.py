def intercalarListas(lista1, lista2):
    listaIntercalada = []
    maior = max(len(lista1), len(lista2))
    for i in range(maior):
        if i < len(lista1):
            listaIntercalada.append(lista1[i])
        if i < len(lista2):
            listaIntercalada.append(lista2[i])

    return listaIntercalada


def main():
    lista1 = [1, 3, 5]
    lista2 = [2, 4, 6, 8, 10]

    listaIntercalada = intercalarListas(lista1, lista2)

    print("-------------------------------")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print("-------------------------------")
    print(f"Lista Intercalada: {listaIntercalada}")


if __name__ == "__main__":
    main()
