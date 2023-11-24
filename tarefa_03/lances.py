u = input()
p = 0
i = 0
lance_vencedor = 0.0
while u != 'F':


    if u.upper() == 'I':
        codigo_produto, lance_minimo = input().split()
        lance_minimo = float(lance_minimo)
        codigo_produto = int(codigo_produto)
        print(f'Bem-vindo ao Leilão de Algoritmópolis! Produto {codigo_produto} com lance mínimo R$ {lance_minimo:.2f}')

    if u.upper() == 'L':
            nome, lance = input().split()
            lance = float(lance)
            
    

            if lance >= lance_minimo and p == 0:
                i = i + 1
                p = p + 1
                lance_vencedor = lance
                nome_vencedor = nome
                print(f'{nome} deu um lance de R$ {lance:.2f}')
            elif lance > lance_vencedor and p == 1:
                i = i + 1
                lance_vencedor = lance
                nome_vencedor = nome
                print(f'{nome} deu um lance de R$ {lance:.2f}')


            else:
                print(f'Lance inválido de {nome}')


    if u.upper() == 'S':
        print(f'Status do Leilão do Produto {codigo_produto}')
    
        if i == 0:
            print('Não houve lances')
        else:
            print(f'{i} lances até agora')
            print(f'{nome_vencedor} deu o melhor lance, de valor R$ {lance_vencedor:.2f}')

    u = input()

print(f'Leilão finalizado com {i} lances')
if i > 0:
    print(f'{nome_vencedor} venceu com o lance de valor R$ {lance_vencedor:.2f}')
else:
    print('Não houve vencedor')

