def eh_data_retroativa(data, banco_de_dados, numero_conta):
    dia_atual = data[0:2]
    mes_atual = data[3:5]
    ano_atual = data[6:]
    
    ultima_data = None
    for i in range(len(banco_de_dados)):
        if banco_de_dados[i][0] == numero_conta:
            ultima_data = banco_de_dados[i][2]

    if ultima_data == None:
        return False

    ultimo_dia = ultima_data[0:2]
    ultimo_mes = ultima_data[3:5]
    ultimo_ano = ultima_data[6:]

    if ultimo_ano > ano_atual:
        return True
    elif ultimo_ano == ano_atual:
        if ultimo_mes > mes_atual:
            return True
        elif ultimo_mes == mes_atual:
            if ultimo_dia > dia_atual:
                return True

    else:
        return False
##########################################################################################################
def compara_data(data1, data2): # data1 = data digitada pelo usuario, data2 = data a ser comparada
    dia1 = data1[0:1]
    dia2 = data2[0:1]
    mes1 = data1[3:4]
    mes2 = data2[3:4]
    ano1 = data1[6:9]
    ano2 = data2[6:9]

    if ano2 > ano1:
        return True
    elif ano1 == ano2:
        if mes2 > mes1:
            return True
        elif mes1 == mes2:
            if dia2 > dia1:
                return True

    else:
        return False
        
##########################################################################################################
def inicializar_contas():
    """
    Devolve um objeto representando o conjunto
    de contas bancárias inicialmente vazio.
    """
    banco_de_contas = {}
    banco_de_dados = []
    
    return banco_de_contas, banco_de_dados
##########################################################################################################
def criar(banco_de_contas, numero_conta):
    """
    Cria uma nova conta identificada por 'numero_conta' com
    saldo 0 e nenhuma movimentação associada.

    Devolve:
        - True se a conta tenha sido criada com sucesso
         -False se já existir conta com esse numero
    """
    
    if numero_conta in banco_de_contas:
        return False


    else:
        return True

def abrir_conta(banco_de_contas):
    """
    Para uma linha com a ação abrir, a próxima linha possui um número de conta. 
    Se uma conta com esse número já existir, deve-se mostrar "Número de conta já existe". 
    Do contrário, deve-se mostrar "Conta aberta com sucesso".
    """
    numero_conta = int(input())
    if criar(banco_de_contas, numero_conta) == True:
        conta = {'saldo': 0}
        banco_de_contas[numero_conta] = conta
        print('Conta aberta com sucesso')
        
        


    elif criar(banco_de_contas, numero_conta) == False:
        print('Número de conta já existe')


##########################################################################################################
def movimentar_deposito(numero_conta, banco_de_contas, data, banco_de_dados):
    """
    Realiza uma movimentação na conta 'numero_conta'
    de valor 'valor' no dia 'data' descrita por 'descricao'.

    Devolve:
        - True se for possível realizar a movimentação
        - False caso contrário.
    """

    if numero_conta in banco_de_contas: # analisa se a conta existe
        if eh_data_retroativa(data, banco_de_dados, numero_conta) == True: # analisa se a data é retroativa 
            print('Movimentação tem data retroativa')
            return False
        else:
            return True
    else:
        print('Esta conta não existe')
        return False
    
def deposito(banco_de_contas, banco_de_dados):
    """
    Para uma linha com a ação depositar, a próxima linha possui um número de conta, o valor do depósito, 
    uma data completa no formato DD/MM/AAAA e a descrição da operação, que é um texto arbitrário. 
    Deve-se contabilizar o depósito e mostrar "Depósito realizado com sucesso".
    """
    informacoes = input().split()
    numero_conta = int(informacoes[0])
    valor = float(informacoes[1])
    data = informacoes[2]
    descricao = informacoes[3:5]

    x = movimentar_deposito(numero_conta, banco_de_contas, data, banco_de_dados)
    if x == True:
        
        banco_de_contas[numero_conta]['saldo'] = banco_de_contas[numero_conta]['saldo'] + valor
        banco_de_contas[numero_conta]['data'] = data
        banco_de_contas[numero_conta]['descricao'] = descricao
        
        operacao = [numero_conta, banco_de_contas[numero_conta]['saldo'], data, 'Depósito', descricao, valor]
        banco_de_dados.append(operacao)

        print('Depósito realizado com sucesso')



    
    
##########################################################################################################

def movimentar_saque(numero_conta, banco_de_contas, data, valor, banco_de_dados):
    """
Realiza uma movimentação na conta 'numero_conta'
de valor 'valor' no dia 'data' descrita por 'descricao'.

    Devolve:
        - True se for possível realizar a movimentação
        - False caso contrário.
    """

    if numero_conta in banco_de_contas: # analisa se a conta existe
        if eh_data_retroativa(data, banco_de_dados, numero_conta) == True: # analisa se a data é retroativa
            print('Movimentação tem data retroativa')
            return False
        else:
            valor = int(valor)
            if banco_de_contas[numero_conta]['saldo'] - valor < 0: # analisa se o usuário tem saldo suficiente pra sacar
                print('Saldo insuficiente')
                return False
            else:
                return True
    else:
        print('Esta conta não existe')
        return False

def saque(banco_de_contas, banco_de_dados):
    """
    Para uma linha com a ação sacar, a próxima linha possui um número de conta, o valor do saque, uma data completa e a descrição da operação. 
    Deve-se contabilizar o saque e mostrar "Saque realizado com sucesso". 
    Caso o saldo da conta não seja suficiente, o programa deve mostrar "Saldo insuficiente".
    """
    
    informacoes = input().split()
    numero_conta = int(informacoes[0])
    valor = float(informacoes[1])
    data = informacoes[2]
    descricao = informacoes[3:5]

    x = movimentar_saque(numero_conta, banco_de_contas, data, valor, banco_de_dados)
    if x == True:
        
        banco_de_contas[numero_conta]['saldo'] = banco_de_contas[numero_conta]['saldo'] - valor
        banco_de_contas[numero_conta]['data'] = data
        banco_de_contas[numero_conta]['descricao'] = descricao
        
        operacao = [numero_conta, banco_de_contas[numero_conta]['saldo'], data, 'Saque', descricao, valor]
        banco_de_dados.append(operacao)
        
        print('Saque realizado com sucesso')



##########################################################################################################
def consultar_saldo(banco_de_contas, numero_conta):
    """
    Devolve o saldo da conta identificada por 'numero_conta'.
    """
    if numero_conta in banco_de_contas:
        print(f"O saldo da conta é R$ {banco_de_contas[numero_conta]['saldo']:.2f}")
    else:
        print('Esta conta não existe')

def consulta_saldo(banco_de_contas):
    """
    Para uma linha com a ação saldo, a próxima linha possui um número de conta. 
    Deve-se computar o saldo e mostrar "O saldo da conta é R$ <saldo>", onde saldo deve ter duas casas decimais.
    """
    numero_conta = int(input())
    consultar_saldo(banco_de_contas, numero_conta)

##########################################################################################################

def fecha_conta(banco_de_contas):
    numero_conta = int(input())
    
    if numero_conta in banco_de_contas:  
        if banco_de_contas[numero_conta]['saldo'] == 0:
            del banco_de_contas[numero_conta]
            print('Conta fechada com sucesso')
        else:
            print('A conta não pode ser fechada')
    else:
        print('Esta conta não existe')

def extrato(banco_de_contas, banco_de_dados):
    """
Para uma linha com a ação extrato, a próxima linha possui um número de conta e uma data de início. 
O programa deve mostrar o extrato das movimentações da conta a partir desta data e mostrar uma sequência de linhas com as movimentações em ordem de realização. 
Para cada movimentação, devem-se mostrar três linhas:

<movimento> de valor R$ <valor> realizado em <dia>/<mes>/<ano>
Descrição adicional: <descricao>
Saldo após movimentação: R$ <saldo_apos>

    """
    numero_conta, data1 = input().split()
    numero_conta = int(numero_conta)
    if numero_conta in banco_de_contas:
        for x in range(len(banco_de_dados)):
            if banco_de_dados[x][0] == numero_conta:
                data2 = banco_de_dados[x][2]
                if compara_data(data1, data2) == True:
                    print(f'{banco_de_dados[x][3]} de valor R$ {banco_de_dados[x][5]:.2f} realizado em {banco_de_dados[x][2]}')
                    print(f'Descrição adicional: {banco_de_dados[x][4]}')
                    print(f'Saldo após movimentação: R$ {banco_de_dados[x][1]}')
    else:
        print('Esta conta não existe')
