velocidade = float(input('Digite a velocidade atual do carro: '))

print('Tenha um bom dia! Dirija com segurança!')

taxa = (velocidade - 80) * 7

if velocidade > 80:
    print('Multado! Você ultrapassou o limite permitido, e sua multa foi de R${:.2f}'.format(taxa))
