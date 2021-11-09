#Dicionario -> A gente que contrala o índice, a chave

import copy
dicionario = {'chave1':'valor da chave'}
dicionario2 = dict(chave1='teste', chave2='Valor')

print(dicionario)
print(dicionario2)

dicionario['chave1'] = 'Novo valor'
dicionario['chave2'] = 'Entrada de valor'

print(dicionario)

if 'naoexiste' in dicionario: #Verifica se a chave existe no diciario
    print(dicionario['naoexiste'])

if dicionario.get('naoexiste') is not None:
    print('Não existe')

dicionario['naoexiste']='Não Existe'

if 'naoexiste' in dicionario: #Verifica se a chave existe no diciario
    print(dicionario['naoexiste'])

dicionario.update({'novo_valor':'Novo Valor'}) # Atualiza o dicionario
del dicionario['novo_valor']

for k,v in dicionario.items():
    print(k,v)

d1 = {1:'a',2:'b'}
v=copy.deepcopy(d1) # Senão colocar o COPY.deepcopy, utiliza a mesma memória do computador


