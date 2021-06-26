#Visualização de dados em Python

import matplotlib.pyplot as plt

x = [1,2]
y = [2,3]


#Título
plt.title("Meu gráfico em python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x,y)
plt.show()