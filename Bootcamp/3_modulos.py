## Módulos

#Organizar logicamente o código

import random

x = lambda y:y+20

n = random.randint(1,99)

adivinhe = int(input('Tente adivinhar um número entre 1 e 99: '))

while n !='adivinhe':
    
    if adivinhe<n:
        
        print('O número é maior que este')

        adivinhe=int(input('Tente outra vez: '))

    elif adivinhe>n:

        print('O número é menor que este')

        adivinhe=int(input('Tente outra vez: '))
    
    else:

        print('Você Acertou!!')

        break
