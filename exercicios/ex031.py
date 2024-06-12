km = float(input('what s distance of the trip?'))
if km <= 200:
    c1 = 0.50 * km
    print('you will have to pay {} dollars for the trip'.format(c1))
else:
    c2 = 0.45 * km
    print('you will have to pay {} dollars for the trip'.format(c2))
