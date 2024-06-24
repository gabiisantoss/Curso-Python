#Catetos e hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co,ca)
print(f'A hipotenusa mede {hip:.2f}')