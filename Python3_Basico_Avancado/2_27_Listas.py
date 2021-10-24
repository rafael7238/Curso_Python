"""
Listas
append,insert,pop,del,clear,extend,+
min,max
range
"""

lista = ["A","B","C","D","E","F"]
string = "NADA"

print(lista[2])
print(lista[::-1]) #Invertendo
print(string[::-1]) #Invertendo

lista.extend(string)
print(lista)

lista = ["A","B","C","D","E","F"]
lista.append(string)
print(lista)

lista = ["A","B","C","D","E","F"]
lista.insert(1,string)
print(lista)

lista = ["A","B","C","D","E","F"]
lista.append(string)
print(lista)
lista.pop()
print(lista)

lista = ["A","B","C","D","E","F"]
del(lista[1:3])
print(lista)

lLista = list(range(1,10))
lSet = set(range(1,10))
print(lLista,lSet)

#-------------
#Jogo da Forca

#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
