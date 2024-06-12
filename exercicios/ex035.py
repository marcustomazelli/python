#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = int(input('Type a length of the first line: '))
b = int(input('Type a length of the second line: '))
c = int(input('Type a length of the third line: '))
list = [a,b,c]
def is_triangle(list):
    if a+b>c:
        if a+c>b:
            if b+c>a:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(is_triangle(list))

