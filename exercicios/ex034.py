salary = float(input('type your salary here for calculate your increase: '))
if salary > 1250:
    increase =  salary + (salary * 0.10)
    print('Your increase is 10%, total is U%{:.3f}'.format(increase))
else:
    increase = salary + (salary * 0.15)
    print('Your increase is 15%, total is U${:.3f}'.format(increase))

