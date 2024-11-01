def media(lista):
    somatorio = 0
    for i in range(len(lista)):
        somatorio += lista[i]

    media = somatorio / len(lista)

    return round(media, 1)


def main():
    temperaturas = [23.5, 18.6, 30.2, 15.9, 25.1, 29.8]
    mediaTemperatura = media(temperaturas)
    print(f"A média das temperaturas {temperaturas} é: {mediaTemperatura}")


if __name__ == "__main__":
    main()
