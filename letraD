# Método Iterativo Linear (M.I.L)
# Função f(x) = 2 * sin(x) - x; [0, 1]; erro < 0.001

from math import *
from sympy import Symbol, diff,sin, cos

a = 0
b = 1
c = Symbol("c")
d = 2 * sin(c)-c
e = diff(d, c)

# Construção teste de convergência
print("*=*====Teste de Convergência===*=*")
print(f"modulo({e}) < 1")
print("Intervalo: -1/2 < cos(c) < 1/2")

f_1 = cos(a)
f_2 = cos(b)

# Caso a condição seja satisfeita
if(f_1 >= -1 / 2 and f_1 <= 1 / 2) or (f_2 >= -1 / 2 and f_2 <= 1 / 2):
  print(f"A função é iterável nos pontos [{a}, {b}]!")

  i = 5
  j = (b + a) / 2
  l = 0
  m = 5

  x = []
  x.append(j)

  while (i > 0.001) or (m > 0.001):
    k = 2 * sin(j)
    x.append(k)

    i = k - j
    m = 2 * sin(k) - k

    if i < 0:
      i = i * (-1)

    if m < 0:
      m = m * (-1)

    j = k

# Resultado da iteração
  print("\n*=*===Resultado Da Iteração===*=*")
  for l in range(len(x)):
    print(f"Iteração {l}: {x[l]}")

# Caso a condição não seja satisfeita
else:
  print(f"A função não é iterável nos pontos [{a}, {b}]!")
