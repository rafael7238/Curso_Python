#tupla -> Não é possível modificar elementos da Tupla, depois que é criado
#Lista -> É POssível

tp = (1,2,3,'a','Rafael Vasconcelos') #Tupla
tp2 = 1,2,3,'a','Rafael Vasconcelos' #Cria um Tupla também

print(tp)

for v in tp:
    print(v,end=' ')
    print('rafael','leite','vasconcelos',sep=';')


tupla = (1,2,3,4)
print(tupla)
lista = list(tupla)
lista[0] = 9
tupla = tuple(lista)
print(tupla)