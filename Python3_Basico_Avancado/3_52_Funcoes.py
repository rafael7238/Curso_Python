def funcao(mensagem):
    print(f"Hello World! {mensagem}")

def saudacao(msg="Olá",nome="Usuário"):
    print(f"{msg} {nome} ")

def funcaoRetorno():
    return "nada"

def f(var):
    print(var)

def dumb():
    return f

def dumb2():
    return('Luiz','Otavio')

def func(*args):
    print(args)
   # args[0]=9 #não é possível alterar uma tupla
    args = list(args)
    args[0]=9
    print(args[0])
    print(len(args))

funcao("nada")
funcao("para nada")

saudacao(msg="nada")
saudacao()
saudacao("Tudo","Bem")

ret = funcaoRetorno()
print(ret)

var = dumb()("teste")

var=dumb2()
print(dumb2(), var[1])

lista=[1,2,3,4,5]
print(lista)
print(*lista) #Desapacotando
print(*lista,sep=",") #Desapacotando

func(1,2,3,4,5,6) 