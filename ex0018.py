from math import radians, sin, cos, tan

ang = float(input('Digite um angulo: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O angulo de {}º tem o seno de {:.2f}'.format(ang, seno))
print('O angulo de {}º tem o cosseno de {:.2f}'.format(ang, cosseno))
print('O angulo de {}º tem a tangente de {:.2f}'.format(ang, tangente))

