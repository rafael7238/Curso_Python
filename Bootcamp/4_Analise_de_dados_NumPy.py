## NUMPY

#Base cientifica que disponibiliza arrays

import numpy as np

#help(np.array)

l=[1,2,3]

x = np.array(l)

print("x: ",x)

print("shape: ",x.shape) #Verifica a dimensão, nesse caso é apenas 1 dimensão

l = [[1,2],[3,4]]

x = np.array(l,dtype=int) #Força o tipo de dados

print("x: ",x)

print("shape: ",x.shape) #Verifica a dimensão, nesse caso são 2 dimensão

print(type(x))

dim = (3,2) #Linhas, Colunas

x=np.zeros(dim) #Cria uma matriz de 0s conforme dimensões

print("x: \n",x)

n=4

x = np.eye(n) #Cria uma matriz identidade
print(x)

x = np.random.random(size=(2,3)) #Criação de uma matriz com valores aleatórios

print(x)

x = np.linspace(start=10,stop=100,num=10)

print(x)

print("Primeiro Elemento: ",x[0])

print("Ultimo Elemento: ",x[-1])

print("Primeiro Elemento: ",x[0:3]) #Slice

print("Primeiro Elemento: ",x[:3]) #Mesma coisa de cima. Usaquando quando priemiro é 0

x = np.random.random(size=(2,3)) #Criação de uma matriz com valores aleatórios

print(x[0,:])