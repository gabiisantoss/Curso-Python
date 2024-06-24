#Seno Cosseno e Tangente
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem \nSENO de {seno:.2f}\n'
      f'COSSENO de {cos:.2f}\n'
      f'TANGENTE de {tan:.2f}')