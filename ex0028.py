from random import randint
from time import sleep


num = int(input('Digite um numero: ')) # jogador tenta adivinhar

print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)

print('Processando...')
sleep(3)

aleatorio = randint(0, 5) # O computador sorteia um número entra 0 e 5

if num == aleatorio:
    print('Você venceu, o número escolhido foi {}!'.format(aleatorio))
else:
    print('Você perdeu, o número escolhido foi {}!'.format(aleatorio))
