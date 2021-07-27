num = int(input('Digite o número: '))

resto = (num % 2)

if resto == 1:
    print('O número {} é ímpar'.format(num))
else:
    print('O número {} é par'.format(num))