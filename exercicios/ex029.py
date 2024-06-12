vel = float(input('enter speed of the car in km/h '))
print('calculating...')
if vel > 80:
    print('you exceeded the speed limit, fined!!')
    multa = 7 * (vel - 80)
    print('you will have to pay {} bucks motherfucker'.format(multa))
else:
    print('you re clear bro, take care')
