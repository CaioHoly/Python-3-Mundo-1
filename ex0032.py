from datetime import date

ano = int(input('Digite um ano qualquer ou coloque 0 para análisar o ano atual: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    ano = date.today().year
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
