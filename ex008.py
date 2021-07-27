valor = float(input('Digite o valor em métros: '))

convert1 = valor / 1000
convert2 = valor / 100
convert3 = valor / 10
convert4 = valor * 10
convert5 = valor * 100
convert6 = valor * 1000

print('A medida de {}m corresponde a'.format(valor))
print('{}km'.format(convert1))
print('{}hm'.format(convert2))
print('{}dam'.format(convert3))
print('{}dm'.format(convert4))
print('{:.0f}Cm'.format(convert5))
print('{:.0f}mm'.format(convert6))
