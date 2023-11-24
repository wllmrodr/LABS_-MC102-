import sys
import modulo_analise as ma
indices = []
paises = []
anos = []
classes = []
duracoes = []


with open("testes/filmes.dat") as f:
    for linha in f:
        indice, pais, ano, classe, duracao = linha.split()
        indices.append(int(indice))
        paises.append(pais)
        anos.append(int(ano))
        classes.append(classe)
        duracoes.append(int(duracao))




def produtividade(inicio, fim):
    """
mostra a quantidade de filmes lançados por ano.
    """
    anos_dentro_do_intervalo = []
    lista_produtividade = []
    intervalo = [i for i in range(inicio, fim+1)]
    
    for c in intervalo:
        if c in anos:
            anos_dentro_do_intervalo.append(c)

    for u in  range(len(intervalo)):
        vezes = anos.count(intervalo[u])
        lista_produtividade.append(vezes)

    for o in range(len(intervalo)):
        print(f'{intervalo[o]}: {lista_produtividade[o]}')





def anos_presentes(inicio, fim):
    """
mostra em ordem crescente, anos nos quais foram lançados filmes.
    """
    lista_filtrada = ma.filtrar_entre(anos, inicio, fim+1)
    lista_sem_repeticoes = ma.remove_duplicatas(lista_filtrada)
    lista_sem_repeticoes.sort()
    for i in lista_sem_repeticoes:
        print(i)


def filmes_por_classificacao(classe):
    """
acha o indice do filme de determinada classe
    """
    lista = []
    for i in range(len(classes)):
        if classe == classes[i]:
            lista.append(indices[i])

    ma.ordena(lista, False)
    
    for c in lista:
        print(c)

def histograma_dos_anos(lista_anos):
    """
mostra a quantidade de filmes lançados em um intervalo de tempo.
    """
    lista = ma.histograma(anos, lista_anos)
    contador = 0

    for u in range(len(lista_anos)-1):
        print(f'[{lista_anos[u]}, {lista_anos[u+1]}): {lista[contador]}')
        contador = contador + 1

def filmes_por_pais_e_classificacao(pais, classe):
    """
acha os indices de filmes de determinada classe e país.
    """
    lista_indices = [] 
    for i in range(len(classes)):
        if classe == classes[i] and pais == paises[i]:
            lista_indices.append(indices[i])
            
    ma.ordena(lista_indices, False)

    for p in lista_indices:
        print(p)
    

   
    
    
def main():
    if sys.argv[1] == 'produtividade':
        inicio, fim = input().split()
        inicio = int(inicio)
        fim = int(fim)
        produtividade(inicio, fim)


    if sys.argv[1] == 'anos_presentes':
        inicio, fim = input().split()
        inicio = int(inicio)
        fim = int(fim)
        anos_presentes(inicio,fim)


    if sys.argv[1] == 'filmes_por_classificacao':
        classe = str(input())
        filmes_por_classificacao(classe)


    if sys.argv[1] == 'histograma_dos_anos':
        lista = list(map(int, input().split()))
        histograma_dos_anos(lista)

    if sys.argv[1] == 'filmes_por_pais_e_classificacao':
        pais, classe = input().split() 
        filmes_por_pais_e_classificacao(pais, classe)

main()
            
