def maximo_recursao(lista, maximo_inicial):
    """
    função responsável apenas por achar o valor máximo da lista de maneira recursiva.
    """
    if len(lista) == 0:
        return maximo_inicial
    
    else:
        if lista[0] > maximo_inicial:
            maximo_inicial = lista[0]
        
        lista.remove(lista[0])
        return maximo_recursao(lista, maximo_inicial)
  


def main():
    """
    função principal, é recebida e entrada e printa a saída.
    """
    maximo_inicial = 0
    lista = list(map(int,input().split()))
    maximo_verdadeiro = maximo_recursao(lista, maximo_inicial)
    print(maximo_verdadeiro)


main()
