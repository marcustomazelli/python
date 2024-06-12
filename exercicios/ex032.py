# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
year = int(input('Type a number to find out if it is a leap year or not. Or type zero for current year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('It s leap year')
else:
    print('it s not leap year')

