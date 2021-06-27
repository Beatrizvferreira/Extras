#Crescimento da população brasileira 1980-2016

dados = open("populacao_brasileira.csv").readlines()
open(dados)

x = []
y = []

for i in range(len(dados)):
    if i!=0:
        linha=dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

print(x)
