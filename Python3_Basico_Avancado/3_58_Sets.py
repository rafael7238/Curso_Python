# Sets não tem Ordens

s1 = {1,2,3,4,5}
print(s1)

s2 = set()
#s2 = {} Cria um dicionário

s2.add(2)
s2.add(4)
s2.discard(4)
s2.update('a')
s2.update('Pyton') # Cada letra será um valor

print(s2)
lista = [1,2,3,4,55555,1,2,3,4]
lista = set(lista) #Tira os duplicados
lista = list(lista)

print(lista)

for v in s1:
    print(v)
#print(s1[0]) #Não há índices

## Comandos

s3 = {1,2,3,4,5,7}
s4 = {1,2,3,4,5,6}

s5 = s1 | s4 #Union
print(s5)

s6 = s3 & s4 #Intersect

s7 = s3 - s4 #Minus

s8 = s3 ^s4 #Minus de toda a direção
