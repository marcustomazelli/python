from math import cos, sin, tan, radians
ang = float(input('let s calculate cos, sin and tangent of right triangle, enter a angle: '))
rad = radians(ang)
c = cos(rad)
s = sin(rad)
t = tan(rad)

print('the sino this angle is: {:.2f}'.format(s))
print('the cosine this angle is: {:.2f}'.format(c))
print('the tangent this angle is: {:.2f}'.format(t))

