#Sorteio de um nome em uma lista
from random import choice
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
nomes = [primeiro,segundo,terceiro,quarto]
sorteio = choice(nomes)
print(f'O aluno sorteado foi {sorteio}')
