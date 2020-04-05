# import math
from math import ceil, sqrt, floor

num = int(input('Digite um número: '))

raiz = sqrt(num)

print('Número digitado {}. Raiz é {}'.format(num, floor(raiz)))