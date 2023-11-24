def historico(numero, sequencia, dicionario):
    """
    função responsável por guardar a resposta de qualquer sequência no dicionario.
    """
    valor = {'sequencia': sequencia}
    dicionario[numero] = valor

def sequencia_pedrinho(numero, dicionario):
    """
    função responsável por calcular a sequência de Pedrinho, de maneira recursiva.
    """

    if numero == 1 or numero == 2 or numero == 3:
        return numero
    elif numero in dicionario:
        return dicionario[numero]['sequencia']
    else:
        sequencia1 = sequencia_pedrinho(numero - 1, dicionario)
        sequencia2 = sequencia_pedrinho(numero - 2, dicionario)
        sequencia3 = sequencia_pedrinho(numero - 3, dicionario)
        
        if numero - 1 not in dicionario:
            historico(numero - 1, sequencia1, dicionario)
        if numero - 2 not in dicionario:
            historico(numero - 2, sequencia2, dicionario)
        if numero - 3 not in dicionario:
            historico(numero - 3, sequencia3, dicionario)
        

        return sequencia1 + 2 * sequencia2 + 3 * sequencia3


def printer(sequencia):
    print(sequencia)

def main():
    """
    função principal, responsável por receber a entrada e printar a saída.
    """
    dicionario = {}
    numero = int(input())
    sequencia = sequencia_pedrinho(numero, dicionario)
    printer(sequencia)

main()
