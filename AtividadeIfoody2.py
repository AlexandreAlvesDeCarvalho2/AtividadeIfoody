kibonSorveteriaSaúde = [4.9,6.99, "kibon Sorveteria Saude"] # coloquei em listas.. 
makisPlace = [4.7,7.99,"Makis Place"]
Sukiya = [4.6,7.99,"Sukiya"]
Giraffas = [4.4,5.99,"Giraffas"]
aFeijoada = [4.4,9.99,"A Feijoada"]
Viena = [4.4,12.49,"Viena"]

notas = [makisPlace,kibonSorveteriaSaúde, Sukiya, Giraffas, aFeijoada, Viena]

notasParaOrdem = [] 
for x in notas:          # criei uma nova lista e negativei o frete para ordem ficar certa.
    x = [x[0],-x[1],x[2]]
    notasParaOrdem.append(x)
    
Classificacao = []       
for x in notasParaOrdem:
    if Classificacao == [] or x < Classificacao[-1]:
        Classificacao.append(x)
    else:
        pos = 0 
        while pos < len(Classificacao):
            if x > Classificacao[pos]:
                Classificacao.insert(pos, x)
                break
            pos += 1

cont=1
for x in Classificacao:
    print("{} - {} com nota {} e frete {}".format(cont,x[2],x[0],-x[1]))
    cont = cont+1
