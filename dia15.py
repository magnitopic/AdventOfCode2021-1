# Numero total de combinaciones con 3 digitos donde num1<num2<num3
digitos = "0123456789"
n = 0    # contador

for p in digitos:
  for q in digitos:
    for r in digitos:
      if p<q<r:
        salto = ""
        if not((n+1)%10): salto='\n'      # salto de línea cada 10 números 
        print(f"{p+q+r} {salto}", end="")
        n += 1

print(f"\nExisten {n} combinaciones.")