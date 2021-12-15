# Divisores de una serie de números
ini = int(input("Inicio: "))
fin = int(input("Final: "))
for n in range(ini, fin+1):
  divisores = []
  for i in range(1, n+1):
    if not(n % i):
      divisores.append(i)
  print(f"{n} -> {divisores}")