print('-=-' * 8)
print('Análisador de triângulos')
print('-=-' * 8)


r1 = float(input('primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triãngulo')
else:
    print('Não é um triângulo')