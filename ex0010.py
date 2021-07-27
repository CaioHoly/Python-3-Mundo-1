carteira = float(input('Quanto de dinheiro você tem na carteira? R$'))

dolar = 3.27

qtd = carteira / dolar

print('com R${:.2f} você pode comprar US${:.2f}'.format(carteira, qtd))
