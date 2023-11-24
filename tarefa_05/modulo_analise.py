def ordena(lista, maior):
    """
    Ordena 'lista' do maior para o menor, caso 'maior' seja True; caso
    contrário, ordena do menor para o maior. Essa função modifica a lista
    passada por parâmetro.

    Parâmetros: lista de números ou strings e um booleano.
    Retorna: nada.
    """
    if maior == True:
        lista.sort(reverse = True)
        
    if maior == False:
        lista.sort()


def moda(lista):
    """
    Encontra a moda de 'lista', isto é, o valor que mais se repete; em caso de
    empate, retorne o que aparece primeiro.

    Parâmetros: lista de strings.
    Retorna: a moda de 'lista'.
    """
    lista.sort()
    lista_repetidos = []
    lista_resto = []
    lista_contadora = []
    c = 1
   
    for i in lista:
        if i not in lista_repetidos:
            lista_repetidos.append(i)
            
        else:
            lista_resto.append(i)

    for x in lista_repetidos:
        for u in lista_resto:
            if x == u:
                c = c + 1 
        lista_contadora.append(c)
    
        c = 1
    
    moda = lista_contadora[0]  
    for y in lista_contadora:
        if lista_contadora[0] < y:
            moda = y

    
    index = lista_contadora.index(moda)
    return lista_repetidos[index]



def mediana(valores):
    """
    Encontra a mediana de 'valores', isto é, o valor que ocupa a posição
    central da lista ordenada. Quando a lista tem tamanho par,
    definimos a mediana como o valor da primeira posição na segunda
    metada da lista ordenada.

    Parâmetros: lista de floats.
    Retorna: a mediana de 'valores'.
    """
    valores.sort()
    if len(valores) % 2 == 0:
        mediana = valores[int(len(valores)/2)]

    else: 
        c = len(valores)
        mediana = valores[int(c/2 - 0.5)]

    return mediana


def media(valores):
    """
    Encontra a média de 'valores'.

    Parâmetros: lista de floats.
    Retorna: a média de 'valores'.
    """
    s = 0
    i = 0
    for i in valores:
        s = s + i
        
    media = s/len(valores)
    
    return media



def media_ponderada(valores, pesos):
    """
    Encontra a média ponderada de 'valores'.

    Parâmetros: listas de floats.
    Retorna: a média ponderada de 'valores'.
    """
    lista_mult = []
    
    divisor = 0
    i = 0
    for i in pesos:
        divisor = divisor + i

    u = 0
    while u < len(valores):
        mult = valores[u] * pesos[u]
        lista_mult.append(mult)
        u = u + 1

    soma = 0
    k = 0
    for k in lista_mult:
        soma = soma + k

    media_p = soma / divisor
    
    return media_p



def filtrar_entre(valores, menor, maior):
    """
    Cria uma lista com os números de 'valores' que estejam no intervalo
    ['menor', 'maior') (o primeiro intervalo é fechado e o segundo é aberto).

    Parâmetros: lista de floats e os limites.
    Retorna: a lista filtrada.
    """
    lista_correta = []
    
    for indice in valores:
        if maior > indice >= menor:
            lista_correta.append(indice)

    return lista_correta


def filtrar_caracteristica(lista, caracteristica, alvo):
    """
    Cria uma lista com os elementos de 'lista' cuja posição em 'caracteristica'
    seja igual a 'alvo'. Por exemplo, com a entrada abaixo, retornaríamos
    ['Alemanha', 'Portugal']:
    lista = ['Brasil', 'Alemanha', 'Angola', 'Portugal']
    caracteristica = ['América do Sul', 'Europa', 'África', 'Europa']
    alvo = 'Europa'

    Parâmetros: listas de números ou strings e um valor alvo.
    Retorna: a lista com a característica filtrada.
    """
    c = 0
    lista_indice = []
    lista_final = []
    for x in caracteristica:
        if x == alvo:
            lista_indice.append(c)
        c = c + 1

    for i in lista_indice:
        lista_final.append(lista[i])

    return lista_final


def histograma(valores, intervalos):
    """
    Cria uma lista com as frequências do histograma de 'valores', divididas nas
    classes conforme a lista 'intervalos'. Por exemplo, se temos [10, 20, 30]
    como intervalos, devemos obter as frequências dos intervalos [10, 20) e [20,
    30).

    Parâmetros: listas de números.
    Retorna: lista de frequência do histograma.
    """
    lista_contadora = []
    for i in range(len(intervalos)-1):
        cont = 0
        for y in valores:
            if intervalos[i+1] > y >= intervalos[i]:
                cont = cont + 1
            
        lista_contadora.append(cont)
            
    return lista_contadora



def maiores_k(valores, k):
    """
    Cria uma lista com os 'k' maiores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k' maiores números.
    """
    valores.sort(reverse = True)
    lista_k_maiores = valores[0:k]
    return lista_k_maiores


def menores_k(valores, k):
    """
    Cria uma lista com os 'k' menores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k'menores números.
    """
    valores.sort()
    lista_k_menores = valores[0:k]
    return lista_k_menores



def remove_duplicatas(lista):
    """
    Cria uma lista removendo todos os elementos duplicados de 'lista', mantendo
    a ordem relativa original. Use somente listas, for/while e variáveis
    simples para implementar essa função.

    Parâmetros: listas de strings.
    Retorna: 'lista' sem duplicatas.
    """
    lista_correta = []
    for i in lista:
        if i not in lista_correta:
            lista_correta.append(i) 

    return(lista_correta)

