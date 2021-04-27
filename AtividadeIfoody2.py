kibonSorveteriaSaúde = [4.9,6.99, "kibon Sorveteria Saude"] # coloquei em listas.. 
makisPlace = [4.7,7.99,"Makis Place"]
Sukiya = [4.6,7.99,"Sukiya"]
Giraffas = [4.4,5.99,"Giraffas"]
aFeijoada = [4.4,9.99,"A Feijoada"]
Viena = [4.4,12.49,"Viena"]

notas = [makisPlace,kibonSorveteriaSaúde, Sukiya, Giraffas, aFeijoada, Viena]

notasParaOrdem = []                             #Criei uma lista nova para negativar o frete
for x in notas:                                 # Para cada elemento em notas
    x = [x[0],-x[1],x[2]]                       # iguala o elemento ao elemento do indice[0], -indice[1], indice[2]                      
    notasParaOrdem.append(x)                    # Adiciona os elementos na lista notasParaOrdem



Classificacao = []                                          #Criei uma nova lista para colocar em ordem
for x in notasParaOrdem:                                    # para cada elemento em notasParaOrdem
    if Classificacao == [] or x < Classificacao[-1]:        # se a lista classificacao estiver vazia ou se o elemento for menor que o ultimo elemento da lista
            Classificacao.append(x)                         # Vai adicionar o elemento por ultimo na lista
    else:
        pos = 0                                             #contador do indice
        while pos < len(Classificacao):                     # enquanto pos for menor que o tamanho da lista 
            if x > Classificacao[pos]:                      # se o elemento for maior que a Classificacao com indice 0, vai inserir o elemento
                Classificacao.insert(pos, x)                                 
                break
            pos += 1                                        # depois que achar o indice certo do elemento, vai adicionar +1 no contador pos, e usar a lógica novamenta até inserir todos os elementos

cont=1
for x in Classificacao:
    print("{} - {} com nota {} e frete {}".format(cont,x[2],x[0],-x[1]))
    cont = cont+1
