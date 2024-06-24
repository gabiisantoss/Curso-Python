#Pintando parede
# 2metros quadrados de parede precisa de 1 litros de tinta
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura 
qtdTinta = area/2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m²\n'
      f'Para pintar essa parede, você precisará de {qtdTinta}l de tinta')