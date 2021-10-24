string="O Brasil é o pais do futebol, o Brasil é penta."
lista = string.split(" ")
print(lista)

for valor in lista:
    print(f"A palavra {valor} apareceu {lista.count(valor)}")

string2 = ','.join(lista)
print(string2)

 