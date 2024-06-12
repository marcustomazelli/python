n1 = int(input('Enter a number: '))
n2 = int(input('Enter a second number: '))
n3 = int(input('Enter a third number: '))
lista = [n1, n2, n3]
ordem = sorted(lista)
print('the largest number is {}'.format(ordem[2]))
print('the smallest number is {}'.format(ordem[0]))