from random import choice
lista = [0, 1, 2, 3, 4, 5]
e = choice(lista)
user = int(input('Can you guess the number the computer is thinking of? Choice a number between 0 to 5: '))
print('The number chosen by computer is {}'.format(e))
if user == e:
    print('congrats, correct! you win')
else:
    print('you lose!! get out of here fatty bitch!')
