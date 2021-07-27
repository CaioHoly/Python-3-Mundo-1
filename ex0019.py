from random import choice

p = str(input('Primeiro nome: '))
s = str(input('Segundo nome: '))
t = str(input('Terceiro nome: '))
q = str(input('Quarto nome: '))

nomes = [p, s, t, q]

aleatorio = choice(nomes)

print('O escolhido entre {}, {}, {} e {} foi {}'.format(p, s, t, q, aleatorio))