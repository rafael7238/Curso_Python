
## STRING

rua = 'Rua do Catete, '

numero = "153, "

bairro = 'Catete, '

cidade ='Rio de Janeiro, '

estado = 'RJ, '

cep = '22220-000'

print(rua)

# Concatenar

endereco = rua+numero+bairro+cidade+estado+cep

print(endereco)

endereco_maiuscula = endereco.upper()

print(endereco)

print(endereco_maiuscula)

print(endereco_maiuscula.title()) #Primeira letra maiuscula

print('xxxxxxxxxxxxxxxxxx')



## INTEGER

x = 50

numero_alunos = int(round(8.5))

print(numero_alunos)

print(type(numero_alunos)) #Saber o Tipo da variável

print('xxxxxxxxxxxxxxxxxx')


## Float

b=-23.8

print(b)

print(type(b))

c=23,4  # É uma tupla

print(c)

print(type(c))

d = 53e3 #numero cientifico

print(d)

print(type(d))

print('xxxxxxxxxxxxxxxxxx')

## Operacoes de Tipos

print(5==5)

print(5==4)

print('Python'=='Python')

print('python'=='Python')

print('AB'>'BC')

print('AB'<'BC')

print('pão'.encode()) #Como foi em memória

print('xxxxxxxxxxxxxxxxxx')


## List

    #Usa Colchetes

    #Permite valores duplicado

    #São Mutáveis - Pode Mudar de lugar

frutas = ['banana','laranja','abacate','melancia','caju']

saldo_alunos = [500,1200,1000,600,5000]

num_paciente=[25,36,50,45,22, 33, 89]

print(frutas)

print(len(saldo_alunos))

frutas.append('Morango')

print(len(frutas))

print(frutas)

saldo_alunos.extend(num_paciente)  # Adiciona uma lista na outra

print(saldo_alunos)

print('xxxxxxxxxxxxxxxxxx')


## Tuple

    #Usa Parênteses

    #Ordenada

    #Permite valores Duplicadas

    #Imutável -> Não permite mudar a ordem

frutas = ('banana','laranja','abacate','melancia','caju')

saldo_alunos = (500,1200,1000,600,5000)

num_paciente= (25,36,50,45,22, 33, 89)

print(frutas[1:3]) #o 3 não é incluso, para isso tem que colocar 4

print(frutas[1:4])

tupla_junta = frutas+ num_paciente + ('Nada','Coisa Nenhuma') #Não existe Append, basta somar as Tuplas

print(tupla_junta)

num_paciente= (25,36,50,45,22, 33, 89,25,36,50,45,22, 33, 89)

print(num_paciente.count(50)) #Quantidade de vezes que aparece determinado valor



#num_paciente.append( #Não eixste Append nas Tuplas

print('xxxxxxxxxxxxxxxxxx')


## Sets

    #Escritos em Chaves

    #Não é ordenado

    #Não permite valores duplicados

    #Não é indexado

cidade = {'Belo Horizonte','Manaus','Fortaleza','Natal'}

print(type(cidade))

print(cidade)

cidade.add('Manaus')

cidade.add('Manaus2')

print(cidade)

print('Manaus' in cidade)

print(len(cidade))

cidade.add('Manaus')

print(len(cidade)) # Não adicionou nenhum

print('xxxxxxxxxxxxxxxxxx')


## Dictionary

    #Escritos em Chaves, e usa ":" para separar as chaves ao valores

cod_uf = {
    21 : 'Maranhão',
    22 : 'Piaui',
    24 : 'Rio Grande do Sul',
    23 : 'Ceará'
}

joao= {
    'cabelo':'preto',
    'olhos':'castanhos'
}

print(cod_uf)

print(cod_uf.values())

print(cod_uf.keys())

print(type(cod_uf))

#variavel_concat = cod_uf + joao

#print(variavel_concat)

print(cod_uf.get(22) + '  -  ' + joao.get('olhos'))

print('xxxxxxxxxxxxxxxxxx')