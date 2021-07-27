nome = input('Tem Silva no nome? ').strip()

dividir = str('SILVA' in nome.upper())
dividirB = dividir.replace('True', 'Tem SILVA no nome').replace('False', 'Não tem SILVA no nome')

print(dividirB)
