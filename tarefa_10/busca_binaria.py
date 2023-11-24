def busca_recursiva(lista, valor_procurado, indice_min, indice_max):
    """
    função responsável por achar o valor procurado de maneira recursiva.
    """
    m = (indice_max + indice_min)//2
    variavel = lista[m]

    if indice_max < indice_min:
        return -1
    
    elif lista[m] == valor_procurado:
        return m

    elif lista[m] > valor_procurado:
        indice_max = m - 1
        
    else: 
        indice_min = m + 1
            

    return busca_recursiva(lista, valor_procurado, indice_min, indice_max)







def main():
    """
    função principal, responsável por receber a entrada e printar a saída.
    """
    lista = list(map(int,input().split()))
    valor_procurado = int(input())

    indice_max = len(lista) - 1
    indice_min = 0

    posicao = busca_recursiva(lista, valor_procurado, indice_min, indice_max)
    print(posicao)


main()
