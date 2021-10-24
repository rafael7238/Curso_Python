# WHILE
while True:
    nome=input("Qual o seu nome? ")
    print(nome)
    print(f"Olá {nome}!")
    break

print("Saiu")

x=0

while x <=10:
    x=x+1
    if x==3:
        continue
    if x+1>11:
        print(x)
    else:
        print(x,end="-")

x=0

while x <=10:
    x=x+1
    if x==3:
        break
    if x+1>11:
        print(x)
    else:
        print(x,end="-")
else:
    print("Else") #Não executa esse comando, por conta do break, o que faz a expressão do While ainda não ser falso
print("Finalizou")

#-------------------------------------
texto="Python"
for letra in texto:
    print(letra)

for n,letra in enumerate(texto):
    print(n,letra)

#Range(start=0,stop,step=1)
for n in range(0,10,1):
    print(n,end="")

print("")
#Range(start=0,stop,step=1)
for n in range(0,10,1):
    print(n,end="")

print()