lista_fechar = []
coordenadas_player = []
c = 0

Px0, Py0, Px1, Py1 = input().split()

Px0 = int(Px0)
Py0 = int(Py0)
Px1 = int(Px1)
Py1 = int(Py1)



n = int(input())
for vezes in range(n):
    Ax0, Ay0, Ax1, Ay1 = input().split()
    
    Ax0 = int(Ax0)
    Ay0 = int(Ay0)
    Ax1 = int(Ax1)
    Ay1 = int(Ay1)
    
    dentro = True

    if Px1 <= Ax0 or Px0 >= Ax1: 
        dentro = False
         

    if Py0 >= Ay1 or Py1 <= Ay0:
        dentro = False

    if dentro == True:
        lista_fechar.append('marcador')
        
        



print(f'Devem ser fechados {len(lista_fechar)} anúncios')

