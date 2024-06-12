# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite
vel = float(input('enter speed of the car in km/h '))
print('calculating...')
if vel > 80:
    print('you exceeded the speed limit, fined!!')
    multa = 7 * (vel - 80)
    print('you will have to pay {} bucks motherfucker'.format(multa))
else:
    print('you re clear bro, take care')
