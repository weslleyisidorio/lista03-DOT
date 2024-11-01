nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]


def maior_que_5(nomes):
    nomes5 = []
    for nome in nomes:
        if len(nome) > 5:
            nomes5.append(nome)

    return nomes5


def main():
    nomes5 = maior_que_5(nomes)
    print(f"Nomes com mais de 5 letras: {nomes5}")


if __name__ == "__main__":
    main()
