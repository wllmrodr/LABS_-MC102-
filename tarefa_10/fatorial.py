def fatorial_recursao(numero):
    """
    função responsável por calcular o fatorial de um número "n", de maneira recursiva, chamando a si mesma em sua definição.
    """
    if numero == 0:
        return 1
        
    elif numero == 1:
        return 1

    return numero * fatorial_recursao(numero - 1)


def main():
    """
    função principal, é recebida e entrada e printa a saída.
    """
    numero = int(input())
    fatorial = fatorial_recursao(numero)
    print(fatorial)


main()
