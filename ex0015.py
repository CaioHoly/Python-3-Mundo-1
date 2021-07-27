diasAlugados = int(input('Quantos dias algados? '))

kmRodados = float(input('Quantos km rodados? '))

total = (diasAlugados * 60) + (kmRodados * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))
