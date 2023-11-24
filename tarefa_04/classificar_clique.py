lista_maliciosa = []
coordenadas_m = []
coordenadas_s = []
coordenadas = []
status = []




m = int(input()) # site maliciosos
for i in range(0,m):
    site_malicioso = input()
    
    if site_malicioso not in lista_maliciosa:
        lista_maliciosa.append(site_malicioso)

n = int(input()) # coordenadas de todos os sites
for u in range(0,n):
    x0, y0, x1, y1, endereço = input().split()
    
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)



    if endereço in lista_maliciosa:
        coordenadas_m.append(x0)
        coordenadas_m.append(x1)
        coordenadas_m.append(y0)
        coordenadas_m.append(y1)
        coordenadas_m.append("m")
        coordenadas.append(coordenadas_m[:])
        coordenadas_m.clear()
    
    else:
        coordenadas_s.append(x0)
        coordenadas_s.append(x1)
        coordenadas_s.append(y0)
        coordenadas_s.append(y1)
        coordenadas_s.append("s")
        coordenadas.append(coordenadas_s[:])
        coordenadas_s.clear()

while True: 

    clique_x, clique_y = input().split()
    clique_x = int(clique_x)
    clique_y = int(clique_y)
    
    if clique_x == -1 and clique_y == -1:
        break
    
    else:
        nenhum = True

        for w in coordenadas:
            
            if  w[0] <= clique_x <= w[1] and w[2] <= clique_y <= w[3]  and w[4] == "m":
                status.append('malicioso')
                nenhum = False
                break 

            if w[0] <= clique_x <= w[1] and w[2] <= clique_y <= w[3]  and w[4] == "s":
                status.append('seguro')
                nenhum = False
                break


        

        if nenhum == True:
            status.append('nenhum')

for u in status:
    print(u)

        

        
