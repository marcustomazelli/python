n1 = int(input('enter a number: '))
n2 = int(input('enter a number: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
rd = n1%n2
e = n1**n2
print('addition is {}, multiplication is {} and division is {:.3f}'.format(s, m, d), end=' ')
# I want to leave only 3 decimal places visible in the answer (f is float number)
# and in final of text i put a command who don´t let the line skip(end=' ')
print('rest of division is {}, integer division is {} and power is {}'.format(rd, di, e))

