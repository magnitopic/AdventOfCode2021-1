# Detectar el número diferente
import random
random.seed()

def genera():
  n = random.randint(3,15) # longitud que tendrá el array
  if random.random()<.5:   # tiramos una moneda a cara o cruz
    array = random.choices(range(-99, 100, 2), k=n-1)     # los n-1 impares
    array.append(random.choice(range(-98, 100, 2)))       # un par
  else:
    array = random.choices(range(-98, 100, 2), k=n-1)     # los n-1 pares
    array.append(random.choice(range(-99, 100, 2)))       # un impar
  random.shuffle(array)  # desordenamos el array para que el nº distinto no esté siempre el último
  return array

def encuentra_el_diferente(array):
  lista = []  # será una lista de casi todos 0 menos un 1, o al contrario
  for num in array:
    lista.append(num%2) # num%2 da 0 si PAR, da 1 si IMPAR
  if sum(lista) == 1: # en este caso en la lista solo hay un impar
    return f"Casi todos pares, el único impar es {array[lista.index(1)]}."
  else:
    return f"Casi todos impares, el único par es {array[lista.index(0)]}."

if __name__ == "__main__":
  array = genera()
  print(array)
  print(encuentra_el_diferente(array))