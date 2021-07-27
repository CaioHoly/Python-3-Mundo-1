from math import hypot

catetoO = float(input('Comprimento do ateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(catetoO, catetoA)

print('A hipotenusa dos comprimentos {} e {} é {:.2f}'.format(catetoO, catetoA, hipotenusa))
