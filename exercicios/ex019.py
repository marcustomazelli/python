from random import choice

print('let s draw a name to fight against demons')

n1 = str(input('enter a name: '))
n2 = str(input('second name: '))
n3 = str(input('third name: '))
n4 = str(input('fourth name: '))
lista = [n1, n2, n3, n4]
e = choice(lista)

print('the person chosen was {}'.format(e))

