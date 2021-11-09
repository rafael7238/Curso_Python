
def func(item):
    return item[1]


def a(x, y): return x*y


print(a(2, 2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 50]
]

print(lista)

lista.sort(key=func, reverse=True)

print(lista)

lista.sort(key=lambda i: i[1])

print(sorted(lista, key=lambda i: i[1]))
lista.sort(key=lambda i: i[1], reverse=True)

print(lista)
