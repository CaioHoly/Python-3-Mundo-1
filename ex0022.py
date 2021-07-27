nome = str(input('Digite seu nome: ')).strip()

maiusculos = nome.upper()

minusculas = nome.lower()

todosA = len(nome) - nome.count(' ')

primeiroA = nome.split()
primeiroB = len(primeiroA[0])

print('Seu nome maiúsculo é {}'.format(maiusculos))
print('Seu nome minúsculo é {}'.format(minusculas))
print('Seu nome tem {} letras tirando os espaços'.format(todosA))
print('Seu primeiro nome é {} e tem {} letras'.format(primeiroA[0], primeiroB))
