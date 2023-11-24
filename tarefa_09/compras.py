def recebe_entradas(): 
    """
    responsável apenas por receber as entradas.
    """

    lista_prod_demanda = list(map(int,input().split()))
    lista_prod_disponivel = list(map(int,input().split()))

    return lista_prod_demanda, lista_prod_disponivel


def analisa_disponibilidade(lista_prod_demanda, lista_prod_disponivel):
    """
    analisa as listas, procurando sequencialmente o determinado produto.
    """
    lista_final = []
    lista_prod_demanda.sort()
    lista_prod_disponivel.sort() 
   
    for x in lista_prod_demanda:
        for y in lista_prod_disponivel:
           if x == y:
               lista_prod_disponivel.remove(y)
               break
        
        else:
            lista_final.append(x)

    
    return lista_final

def mostrador(lista_final):
    """
    responsável apenas por imprimir a saída.
    """
    for x in lista_final:
        print(f'{x}', end=' ') #arrumar o jeito de mostrar na tela
        
    print()



def main():
    lista_prod_demanda, lista_prod_disponivel = recebe_entradas()
    lista_final  = analisa_disponibilidade(lista_prod_demanda, lista_prod_disponivel)
    mostrador(lista_final)

main()
