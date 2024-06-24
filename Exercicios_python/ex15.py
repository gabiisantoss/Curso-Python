#Aluguel de carros
qtdKm = float(input('Qual a quantidade de km rodados? '))
qtdDias = int(input('Quantidade de dias alugados? '))
# 60 por dia + 0,15 por km
preco = (60*qtdDias) + (0.15*qtdKm)
print(f'O total a pgar é de R${preco:.2f}')
