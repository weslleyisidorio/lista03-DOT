def vogal(listaPalavras):
    iniciaVogal = []
    for palavra in listaPalavras:
        if palavra[0] in "aeiouAEIOU":
            iniciaVogal.append(palavra)

    return iniciaVogal


def main():
    palavras = ["gato", "elefante", "urso", "abelha", "cobra"]
    iniciaVogal = vogal(palavras)
    print(f"Palavras da lista {palavras} que iniciam com vogal: {iniciaVogal}")


if __name__ == "__main__":
    main()
