from random import shuffle

print('let s organize names to show your homework')

n1 = str(input('enter a name: '))
n2 = str(input('second name: '))
n3 = str(input('third name: '))
n4 = str(input('fourth name: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('the order is {}'.format(lista))
