soma = 0
nomes = []
N, Q, V, M, a, b = input().split()
N = int(N)
Q = int(Q)
V = int(V)
M = float(M)
i = 0

while i<N:

    nome, q, v = input().split()
    q = int(q)
    v = int(v)

    if v == 0:
        m=0
    elif v == 1:
        valor = float(input())
        m = valor
    else:
        for P in range(0,v):
            valor=float(input())
            soma+=valor
        m=soma/v

    if (v >= V and m >= M) or q>=Q: 
        nomes.append(nome)
    elif nome[0] == a or nome[0] == b:
        nomes.append(nome)
    i+=1
    soma = 0



for nome in nomes:
    print(nome)






