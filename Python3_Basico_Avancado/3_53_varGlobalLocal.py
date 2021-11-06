variavelGlobal  = 10
variavelGlobal2 = 10

def func():
    variavelGlobal = 20
    global variavelGlobal2 
    variavelGlobal2 = 30
    print(variavelGlobal)

func()
print(variavelGlobal)
print(variavelGlobal2)