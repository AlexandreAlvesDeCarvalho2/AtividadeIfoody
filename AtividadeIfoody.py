kibonSorveteriaSaúde = [4.9,6.99, "kibon Sorveteria Saude"] # coloquei em listas.. 
makisPlace = [4.7,7.99,"Makis Place"]
Sukiya = [4.6,7.99,"Sukiya"]
Giraffas = [4.4,5.99,"Giraffas"]
aFeijoada = [4.4,9.99,"A Feijoada"]
Viena = [4.4,12.49,"Viena"]

classificacao = [makisPlace,kibonSorveteriaSaúde, Sukiya, Giraffas, aFeijoada, Viena] # coloquei todas as listas em outra lista
classificacao.sort(key = lambda x : (-x[0], x[1]))

Lugar1 = classificacao[0]  #fiz uma atribuição pra ter acesso a listas
Lugar2 = classificacao[1]
Lugar3 = classificacao[2]
Lugar4 = classificacao[3]
Lugar5 = classificacao[4]
Lugar6 = classificacao[5] 

Posicao = [Lugar1,Lugar2,Lugar3,Lugar4,Lugar5,Lugar6]

cont=1
for x in Posicao:
    print("{} - {} com nota {} e frete {}".format(cont,x[2],x[0],x[1]))
    cont = cont+1
