def insere_na_lista(n):
    """
insere a entrada numa lista.
    """
    lista_de_sinais = []
    for i in range(n):
        sinal = list(map(float, input().split()))
        lista_de_sinais.append(sinal)

    return lista_de_sinais

#########################################################################################

def le_entrada():
    """
recebe a entrada e cria uma lista de listas.
    """

    
    n = int(input())
    lista_de_sinais = insere_na_lista(n)

    return lista_de_sinais

#########################################################################################

def analisa_frequencias(lista_de_sinais):
    """
compara as listas e analisa seu tipo.
    """
    c = 0
    d = c + 1
    relatorio = []

    while c != len(lista_de_sinais):
        if len(lista_de_sinais[c]) == len(lista_de_sinais[d]):
            teste = 'igual'
            relatorio.append(teste)


        elif len(lista_de_sinais[c]) % len(lista_de_sinais[d]) == 0:
            teste = 'multiplo'
            relatorio.append(teste)

        elif len(lista_de_sinais[c]) % len(lista_de_sinais[d]) != 0:
            teste = 'diferente'
            relatorio.append(teste)

        c = c + 1
    
    if 'diferente' in relatorio: # coloca função de rejuste de freq. arbitrárias
        resultado = 'freq.arbitraria'
        return resultado

    elif 'multiplo' in relatorio: # coloca função de rejuste de freq. múltiplas
        resultado = 'freq.multipla'
        return resultado

    elif 'igual' in relatorio: # coloca função de rejuste normal (média)
        resultado = 'freq.igual'
        return resultado

#########################################################################################

def acha_menor(lista_de_sinais):
    lista_de_tamanhos = []
            
    for x in lista_de_sinais:
        if len(x) not in lista_de_tamanhos:
            lista_de_tamanhos.append(len(x))

    lista_de_tamanhos.sort()

    menor = lista_de_tamanhos[0]
    return menor

#########################################################################################

def reamostrador_simples(lista_de_sinais):
        """
    com as listas de frequências de mesmo tamanho, é responsável apenas por calcular a média e printar o resultado.
        """
        lista_final = []
        linha = len(lista_de_sinais)
        coluna = len(lista_de_sinais[0])

        for i in range(coluna):
            soma = 0
            for j in range(linha):
                soma += lista_de_sinais[j][i]
            media = soma/linha
            lista_final.append(media)

        for i in lista_final:
            print(f'{i:.2f} ', end = '')
        
        print()

#########################################################################################

def reamostrador_complexo_1(lista_de_sinais):
        """
    responsável por arrumar as listas de freq. múltiplas    
        """

        menor = acha_menor(lista_de_sinais)
        if menor == 0:
            return None


        lista_de_d = []
        
        for i in lista_de_sinais:
            tamanho = len(i)
            d = tamanho / menor
            lista_de_d.append(int(d))

        lista_final = []

        for l in range(len(lista_de_d)):
            if (lista_de_d[l] == 1):
                lista_final.append(lista_de_sinais[l])
            
            else:
                acumula = 0
                posicao = 0
                linha = []

                while (acumula != len(lista_de_sinais[l])):
                    varia = 0

                    for g in range(lista_de_d[l]):
                        varia = varia + lista_de_sinais[l][posicao]
                        posicao = posicao + 1
                    
                    varia = varia/lista_de_d[l]
                    linha.append(varia)
                    acumula = acumula + lista_de_d[l]

                lista_final.append(linha)
        
        reamostrador_simples(lista_final)

#########################################################################################

def reamostrador_complexo_2(lista_de_sinais):
        """
    reponsável por arrumar as listas de freq.arbitrarias
        """
        import math 

        menor = acha_menor(lista_de_sinais)
        if menor == 0:
            return None

        lista_de_d = []
        
        for i in lista_de_sinais:
            tamanho = len(i)
            d = tamanho / menor
            lista_de_d.append(d)

        lista_final = []
        
        for i in range(len(lista_de_d)):
            x = f'{lista_de_d[i]:.2f}'
            x = float(x)
            lista_de_d[i] = x

        for l in range(len(lista_de_d)):
            if (lista_de_d[l] == 1):
                lista_final.append(lista_de_sinais[l])

            else:
                acumula = 0
                posicao = 0
                ref = 0
                linha = list()
                
                while(acumula != len(lista_de_sinais[l])):
                    varia = 0
                    ref = ref + 1
                    diferenca = math.ceil(lista_de_d[l] * ref) - math.ceil(acumula) 
                    if diferenca != 0:
                        
                        for j in range(diferenca):
                            varia = varia + lista_de_sinais[l][posicao]
                            posicao = posicao + 1
                        varia = varia / diferenca
                        
                    linha.append(varia)
                    acumula = (lista_de_d[l] * ref)

                lista_final.append(linha)

        reamostrador_simples(lista_final)

#########################################################################################

def devolve_freq_comprimida(resultado, lista_de_sinais):
    """
recebe o marcador e redireciona pra função final devida.
    """

    if resultado == 'freq.igual':
        reamostrador_simples(lista_de_sinais)

    if resultado == 'freq.multipla':
        reamostrador_complexo_1(lista_de_sinais)

    if resultado == 'freq.arbitraria':
        reamostrador_complexo_2(lista_de_sinais)

#########################################################################################

def main():
    """
função principal.
    """
    lista_de_sinais = le_entrada()
    resultado = analisa_frequencias(lista_de_sinais)
    devolve_freq_comprimida(resultado, lista_de_sinais)


main()

