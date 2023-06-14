# Método Iterativo Linear (M.I.L)
# Função f(x) = e ** x - tg(x); [0, 1]; erro < 0.001

from math import *
from sympy import Symbol, diff, sin, cos, tan 

eul = 2.718
a = 0
b = 1
c = Symbol("c")
d = - tan(c)
e = diff(d, c)

# Construção do teste de convergência
print("*=*====Teste de Convergência===*=*")
print(f"modulo(e**c{e}) < 1")
print("Intervalo: -1 < e**c - tan(c)**2 < 1")

f_1 = eul ** (a) - tan(a) ** 2
f_2 = eul ** (b) - tan(b) ** 2

# Caso a condição seja respeitada
if(f_1 >= -1 and f_1 <= 1) and (f_2 >= -1 and f_2 <= 1):
  print(f"A função é iterável nos pontos [{a}, {b}]!")

  i = 5
  j = (b + a) / 2
  l = 0
  m = 5

  x = []
  x.append(j)

  while (i > 0.001) or (m > 0.001):
    if l == 50:
      break

    k = (tan(j)* j) / (eul ** j) 
    x.append(k)

    i = k - j
    m = eul ** k - tan(k)

    if i < 0:
      i = i * (-1)

    if m < 0:
      m = m * (-1)

    j = k
    l = l + 1

  l = 0

# Amostragem da iteração dos pontos
  print("\n*=*===Resultado Da Iteração===*=*")
  for l in range(len(x)):
    print(f"Iteração {l}: {x[l]}")

# Caso não seja iterável
else:
  print(f"A função não é iterável nos pontos [{a}, {b}]!")
