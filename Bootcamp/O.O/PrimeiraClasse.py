class Animal:
    pass

    def oi(obj):
        print('Miuai..Eu sou o gato '+ obj.nome + '!')

    def __init__(self):
        print('__init__ foi executado')

class Pessoa:
    pass

    def __init__(self):
       print('2')

    def __init__(self,nome,idade):
        print('3')

if __name__ == '__main__':

    x=Animal()
    
    y=Animal()

    p=Pessoa()

    x.nome='Gato'

    x.ano_nascimento='2020'

    y2 = y

    print(x.nome)
    
    print(y==y2)
    
    print(y==x)

    print(x.__dict__) #busca todas as variaveis da classe

    print(Animal.oi(x))