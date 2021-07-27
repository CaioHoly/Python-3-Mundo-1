valor = float(input('Qual é o sálario do funcionário? R$'))

resultado = valor + (valor * 15 / 100)

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(valor, resultado))
