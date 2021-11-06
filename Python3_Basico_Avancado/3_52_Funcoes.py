def funcao(mensagem):
    print(f"Hello World! {mensagem}")


def saudacao(msg="Olá", nome="Usuário"):
    print(f"{msg} {nome} ")


def funcaoRetorno():
    return "nada"


def f(var):
    print(var)


def dumb():
    return f


def dumb2():
    return('Luiz', 'Otavio')


def func(*args):
    print(args)
   # args[0]=9 #não é possível alterar uma tupla
    args = list(args)  # Transformando para uma lista
    args[0] = 9
    print(args[0])
    print(len(args))


def funcNone(nome="", sobrenome=None):
    print(f"Nome: {nome} Sobrenome: {sobrenome}")


def funcArgs(*args):
    print(args)


def funcArgsKwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs["teste"], kwargs["nome"])

    verificarExisteVariavel = kwargs.get('teste')
    if verificarExisteVariavel is not None:
        print(kwargs["teste"])

    verificarExisteVariavel = kwargs.get('nada')
    if verificarExisteVariavel is not None:
        print(kwargs["teste"])


funcao("nada")
funcao("para nada")

saudacao(msg="nada")
saudacao()
saudacao("Tudo", "Bem")

ret = funcaoRetorno()
print(ret)

var = dumb()("teste")

var = dumb2()
print(dumb2(), var[1])

lista = [1, 2, 3, 4, 5]
print(lista)
print(*lista)  # Desapacotando
print(*lista, sep=",")  # Desapacotando

func(1, 2, 3, 4, 5, 6)

funcNone()
funcNone("Rafael", "Vasconcelos")

funcArgs([1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12])
funcArgs(*[1, 2, 3, 4, 5, 6, 7], *[8, 9, 10, 11, 12])

funcArgsKwargs(*[1, 2, 3, 4, 5, 6, 7], *[8, 9, 10, 11, 12],
               teste="nada", nome="Rafael", *[1, 23, 4])
