import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    vetor.append(random.randint(0,50))

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()