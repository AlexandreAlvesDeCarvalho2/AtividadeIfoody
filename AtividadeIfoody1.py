kibonSorveteriaSaúde = [4.9,6.99, "kibon Sorveteria Saude"] # coloquei em listas.. 
makisPlace = [4.7,7.99,"Makis Place"]
Sukiya = [4.6,7.99,"Sukiya"]
Giraffas = [4.4,5.99,"Giraffas"]
aFeijoada = [4.4,9.99,"A Feijoada"]
Viena = [4.4,12.49,"Viena"]

restaurantes = [makisPlace,kibonSorveteriaSaúde, Sukiya, Giraffas, aFeijoada, Viena] # coloquei todas as listas em outra lista

notasParaOrdem = []                             #Criei uma lista nova para negativar o frete e não interferir na lista principal
for x in restaurantes:                          # Para cada elemento em notas
    x = [x[0],-x[1],x[2]]                       # iguala o elemento ao elemento do indice[0], -indice[1], indice[2]         
    notasParaOrdem.append(x)  

notasParaOrdem.sort()                           # Classificação dos elementos

cont=1
for x in notasParaOrdem:
    print("{} - {} com nota {} e frete {}".format(cont,x[2],x[0],-x[1]))
    cont = cont+1
