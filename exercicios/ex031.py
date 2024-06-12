# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('what s distance of the trip?'))
if km <= 200:
    c1 = 0.50 * km
    print('you will have to pay {} dollars for the trip'.format(c1))
else:
    c2 = 0.45 * km
    print('you will have to pay {} dollars for the trip'.format(c2))
