from random import shuffle

p = str(input('Primeiro nome: '))
s = str(input('Segundo nome: '))
t = str(input('Terceiro nome: '))
q = str(input('Quarto nome: '))

lista = [p, s, t, q]

shuffle(lista)

print(lista)
