#Visualização de dados em Python
#Gráfico de dispersão ou gráfico de pontos


import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [100,50,150,100,50]


titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x,y, label = "Meus pontos", color="red", marker="*", s=z)
plt.legend()
plt.show()
#plt.savefig("figura1.png",dpi=300 )
#dpi (aumenta o tamanho da figura e qualidade)


'''
color: cor 
label: rótulo
linestyle: estilo de linha 
linewidth: largura da linha
marker: marcador 
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''