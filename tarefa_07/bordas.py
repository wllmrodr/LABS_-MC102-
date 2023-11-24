def le_arquivo_img(arquivo_pbm):
    """
lê o arquivo pbm e devolve uma matriz.
    """
    with open(arquivo_pbm) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        largura, altura = arquivo.readline().strip().split()

        matriz = []
        largura = int(largura)
        altura = int(altura)

        for linha in arquivo:
            matriz.append(linha.strip().split())

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(matriz[i][j])


    return tipo_arquivo, largura, altura, matriz

##################################################################################################

def eh_borda(matriz, i, j):
    """
analisa determinado pixel para classificar o mesmo como pixel da borda ou não.
    """
    if matriz[i-1][j-1] == 0 or matriz[i-1][j] == 0 or matriz[i-1][j+1] == 0 or matriz[i][j-1] == 0 or matriz[i][j+1] == 0 or matriz[i+1][j-1] == 0 or matriz[i+1][j] == 0  or matriz[i+1][j+1] == 0:
        return True
    else: 
        return False
##################################################################################################

def faz_nova_matriz(matriz, largura, altura):
    """
é responsável por criar um novo arquivo apenas com os pixels da borda.
    """
    linhas = altura
    colunas = largura
    lista_de_lista = []
    lista = []

    for i in range(linhas):
        lista = []
        for j in range(colunas):

            if matriz[i][j] == 0:
                lista.append(0)
            elif matriz[i][j] == 1:
                if eh_borda(matriz, i, j) is True:
                    lista.append(1)
                elif eh_borda(matriz, i, j) is False:
                    lista.append(0)
        

        lista_de_lista.append(lista)

    return lista_de_lista

##################################################################################################
def escreve_no_arquivo(tipo_arquivo, largura, altura, matriz, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(tipo_arquivo + '\n')
        arquivo.write(str(largura) + ' ' + str(altura) + '\n')

        for o in range(altura):
            for p in range(largura):
                arquivo.write(str(matriz[o][p]) + ' ') 
            arquivo.write('\n')



##################################################################################################

def main():
    import sys
    arquivo_pbm = sys.argv[1]
    nome_arquivo = sys.argv[2]
    tipo_arquivo, largura, altura, matriz = le_arquivo_img(arquivo_pbm)
    matriz_nova = faz_nova_matriz(matriz, largura, altura)
    escreve_no_arquivo(tipo_arquivo, largura, altura, matriz_nova, nome_arquivo)

##################################################################################################

main()
