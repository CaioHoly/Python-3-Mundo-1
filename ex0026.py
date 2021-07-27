frase = str(input('Digite uma frase: ').strip()).upper()

contador = frase.count('A')

primeira = frase.find('A')
ultima = frase.rfind('A')

print('A letra A apareceu {} vezes na frase.'.format(contador))
print('A primeira vez que a letra A aparece é na {} linha'.format(primeira+1))
print('A última vez que a letra A parece é na {} linha'.format(ultima+1))
