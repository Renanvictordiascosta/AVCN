# Método da Iteração Linear (M.I.L)
# Função f(x) = tan(2 * x) - x; [0, 1]; erro < 0.001

from math import *
from sympy import Symbol, diff,sin, cos, tan

a = 0
b = 1
c = Symbol("c")
d = tan(2 * c)-c
e = diff(d, c)

# Construção do teste de convergễncia
print("*=*===Teste de Convergência===*=*")
print(f"modulo({e}) < 1")
print(f"Intervalo: {-(1/2)**(1/2)} < t(2*c) < {(1/2)**(1/2)}")

f_1 = tan(2 * a)
f_2 = tan(2 * b)

# Condicional caso seja iterável
if(f_1 >= -(1/2)**(1/2) and f_1 <= (1/2)**(1/2)) or (f_2 >= -(1/2)**(1/2) and f_2 <= (1/2)**(1/2)):
  print(f"A função é iterável nos pontos [{a}, {b}]!")

  i = 5
  j = (b + a) / 2
  l = 0
  m = 5

  x = []
  x.append(j)

  while (i > 0.001) or (m > 0.001):
    if l == 10000:
      break

    k = tan(2 * j)
    x.append(k)

    i = k - j
    m = tan(2 * k) - k

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

# Caso não seja iterável no ponto
else:
  print(f"A função não é iterável nos pontos [{a}, {b}]!")
