# Exercício 3 - Aula 5
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Para o ângulo {} o seno é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}.'.format(angulo, seno, coseno, tangente))

