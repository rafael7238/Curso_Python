l1 = [1,2,3,4,5,6,7,8,9]

l2 = [varial*2 for varial in l1]

l3 = [(v,v2) for v in l1 for v2 in range(3)]

tuplas = (('chave 1', 'valor'),('chave 2','valor 2'))

lista = [(x,y) for x,y in tuplas]
print(lista)
lista = [(y,x) for x,y in tuplas]
print(lista)

print(l1)
print(l2)
print(l3)

l3 = list(range(100))
print(l3)
ex6 = [v for v in l3 if v % 3==0 if v % 8 ==0] #Divisiveis por 3 e por 8
ex7 = [v if v%3 ==0 and v%8 ==0 else 0 for v in l3 ]
print(ex6)
print(ex7)