# Método Iterativo Linear (M.I.L.)
# Função f(x) = sin(2x) - x; [0, 1]; erro < 0.001

from math import *
from sympy import Symbol, diff, sin, cos

a = 0
b = 1
c = Symbol("c")
d = sin(2*c)-c
e = diff(d, c)

# Construção do teste de convergência
print("*=*====Teste de Convergência===*=*")
print(f"modulo({e}) < 1")
print("Intervalo: -1/2 < cos(2*c) < 1/2")

f_1 = cos(2 * a)
f_2 = cos(2 * b)

# Condicional de validação se é iterável
if(f_1 >= -1/2 and f_1 <= 1/2) or (f_2 >= -1/2 and f_2 <= 1/2):
  print(f"A função é iterável nos pontos [{a}, {b}]!")

  i = 5
  j = (b + a) / 2
  l = 0
  m = 5

  x = []
  x.append(j)

  while (i > 0.001) or (m > 0.001):
    if l == 1000:
      break

    k = sin(2 * j)
    x.append(k)

    i = k - j
    m = sin(k) - k

    if i < 0:
      i = i * (-1)

    if m < 0:
      m = m * (-1)

    j = k
    l = l + 1

  l = 0

# Pontos iterados
  print("\n*=*===Resultado Da Iteração===*=*")
  for l in range(len(x)):
    print(f"Iteração {l}: {x[l]}")

# Caso não seja iterável
else:
  print(f"A função não é iterável nos pontos [{a}, {b}]!")
