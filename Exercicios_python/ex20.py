#Sorteio de uma ordem de uma lista
from random import shuffle
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
nomes = [primeiro,segundo,terceiro,quarto]
shuffle(nomes)
print(f'A ordem será  {nomes}')
