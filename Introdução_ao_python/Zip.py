#Função ZIP 
'''
A função zip concatena listas
'''

lista1 = [1,2,3,4,5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = ["R$ 2,00","R$ 5,00","não tem preço","não tem preço","não tem preço"]

for numero,nome,preço in zip(lista1,lista2,lista3):
    print(numero,nome,preço)