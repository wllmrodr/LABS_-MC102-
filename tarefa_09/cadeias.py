def recebe_moleculas():
    """
    responsável apenas por receber as "m" moléculas.
    """
    cadeia = []
    m = int(input())
    for x in range(m):
        molecula = list(map(int,input().split()))
        molecula.sort()
        cadeia.append(molecula)

    return cadeia

def ordena(trios):
    # bubble sort para ordenar os trios
    tamanho = len(trios)

    for i in range(tamanho - 1):
        for j in range(tamanho - 1):
            if trios[j][0] > trios[j + 1][0]:
                var_aux = trios[j]
                trios[j] = trios[j + 1]
                trios[j+1] = var_aux

def analisa_moleculas(cadeia):
    """
    analisa cada molecula e define se o conjunto é um trio que forma uma cadeia forte ou não.
    """

    primeiros_elementos = set()
    lista_trios = []
    lista_dict = []

    for i in range(len(cadeia)): #acha todos os primeiros elementos, sem repetir
        primeiros_elementos.add(cadeia[i][0])

    for primeiro in primeiros_elementos: #acha a ligação entre primeiros elementos e os demais
        lista_elementos = []

        for indice in range(len(cadeia)): 
            if primeiro == cadeia[indice][0]:
                lista_elementos.append(cadeia[indice][1])
        lista_elementos.sort()

        dicionario = {
        'primeiro': primeiro,
        'lista' : lista_elementos
        }

        lista_dict.append(dicionario)


#Verifico tamanho da lista
#pego o primeiro elemento e procuro no dicionario
#se o elemento existir vejo se possui algum numero q esteja na lista1
#se o elemento existir crie o trio, senão passa para o proximo!

    for i in range(len(lista_dict)): #percorre a lista de dicionarios

        lista = lista_dict[i]['lista'] # lista do i-ésimo dicionario
        primeiro = lista_dict[i]['primeiro'] # primeiro do i-ésimo dicionario
        tamanho = len(lista)
        if tamanho < 2: # verifica se pode formar um trio
            continue 
        else:
            for j in range(tamanho): # confirma se esse trio realmente existe, procurando nas listas do dicionário.
                numero_lista = lista[j]
                for k in range(len(lista_dict)):
                    if lista_dict[k]['primeiro'] == numero_lista: # Se encontrarmos o elemento 'numero_lista' verificamos a sua lista pra ver se algum elemento esta na lista em análise
                        lista2 = lista_dict[k]['lista']
                        for l in lista2:
                            if l in lista:
                                linha = [primeiro, numero_lista, l]
                                lista_trios.append(linha)

    ordena(lista_trios)
    return lista_trios


def mostrador_de_trios(lista_trios):
    """
    responsável apenas por printar os trios definidos.
    """
    for indice in range(len(lista_trios)):
        print(f"{lista_trios[indice][0]} {lista_trios[indice][1]} {lista_trios[indice][2]}" )
    

def main():
    cadeia = recebe_moleculas()
    lista_trios = analisa_moleculas(cadeia)
    mostrador_de_trios(lista_trios)

main()
