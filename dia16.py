# Comprobador de letras repetidas
frase = "Un hombre sólo tiene derecho a mirar a otro hacia abajo, cuando ha de ayudarle a levantarse."  # Gabriel García Márquez

def depura(frase):                 # depuramos la frase eliminando signos de puntuación y acentos
  frase = frase.replace(',', '')
  frase = frase.replace('.', '')
  frase = frase.replace('á', 'a')
  frase = frase.replace('é', 'e')
  frase = frase.replace('í', 'i')
  frase = frase.replace('ó', 'o')
  frase = frase.replace('ú', 'u')
  return frase

def caracteres_repetidos(frase):
  palabras = []    # lista de palabras con caracteres repetidos
  todas = frase.split(' ')
  for palabra in todas:
    repe = False                     # bandera
    for caracter in palabra:
      if palabra.count(caracter)>1:
        repe = True
    if repe:
      palabras.append(palabra)
  return palabras

con_repetidos = caracteres_repetidos(depura(frase))
print(con_repetidos)
print(f"La frase inicial tiene {len(frase.split(' '))} palabras y de ellas tienen caracteres repetidos {len(con_repetidos)} palabras.")