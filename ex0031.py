kms = float(input('Qual a distância de sua viagem: '))

print('Você está prestes a começar uma viagem de {}Km'.format(kms))

if kms <= 200:
    valor = kms * 0.50
else:
    valor = kms * 0.45

print('Sua passagem vai custar R${:.2f}.'.format(valor))
