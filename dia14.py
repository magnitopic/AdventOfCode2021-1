# Separar elementos de una lista
import random
random.seed()
digitos = "0123456789"
letras_simbolos = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZºª\!|@#~€¬·$%&/()=?¿*+{}[].-:_><"
true_false = (True, False)  # tupla
lista = []
numeros = []
letras = []
booleanos = []

for i in range(20):
  rnd = random.random()
  if rnd < 0.45:
    lista.append(random.choice(digitos))
  elif rnd < 0.8:
    lista.append(random.choice(letras_simbolos))
  else:
    lista.append(random.choice(true_false))

print(f"Lista original:     {lista}")

for element in lista:
  if str(element) in digitos:
    numeros.append(element)
  elif str(element) in letras_simbolos:
    letras.append(str(element))
  else:
    booleanos.append(element)

print(f"Números:            {numeros}")
print(f"Letras y símbolos : {letras}")
print(f"Booleanos:          {booleanos}")