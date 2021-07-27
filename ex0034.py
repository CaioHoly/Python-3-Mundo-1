salario = float(input('Qual é o sálario do funcionário? R$'))

if salario <= 1250:
    aumento = salario * 1.15
    print('Seu sálario teve aumento de 15% e foi para R${:.2f}'.format(aumento))
else:
    aumento = salario * 1.10
    print('Seu sálario teve um aumento de 10% e foi para R${:.2f}'.format(aumento))
