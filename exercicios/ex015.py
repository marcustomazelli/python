print('rent cars. 60 bucks per day and 0,15 per km ')
day = int(input('how many days u used the car? '))
km = float(input('how many km driven? '))

c = (60 * day) + (0.15 * km)

print('you ll have to pay {:.2f} bucks buddy :)'.format(c))
