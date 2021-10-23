
## If

a=50

b=100

c=50

if (a==b):
    
    print('a igual a b')

elif(b==c):
    
    print('b igual a c')

elif(a==c):
    
    print('a igual a c')

else:
    
    print('Todos os valores são diferente')

print('XXXXXXXXXXXXXX')

## For

cor = ['verde','amarelo','azul','cinza','vermelho']

for x in cor:
    
    print(x)

print('XXXXXXXXXXXXXX')

for x in 'Rafael':
    
    if (x=='a'):
        
        print('valor a')
        
        continue

    if(x=='l'):
        
        break

    print(x)

print('XXXXXXXXXXXXXX')

## While

num = 1


while num<10:

    print(num)
    
    num=num+1

print('XXXXXXXXXXXXXX')


## Range
 # range(inicio,termino,salto) 

for i in range(1,10):

    print(i)
 

for i in range(1,10,2):

    print(i)


print('XXXXXXXXXXXXXX')


## Def

def soma(x,y):

    return (x+y)

print(soma(2,10))

print('XXXXXXXXXXXXXX')


## Lambda (Funções Anônimas)

soma2 = lambda x,y : x+y

print(soma2(10,2))

lista = [1,5,4,6,8,11,3,12]

nova_lista = list(filter(lambda x: (x%2==0),lista))

print(nova_lista)

print('XXXXXXXXXXXXXX')