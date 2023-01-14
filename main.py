"""nombre = input("ingrese su nombre")
apellido = input("ingrese el apellido")
edad = input("ingrese su edad")

fullname = "hola" + "mi nombre es" + nombre + "mi apellido es" + apellido + "y tengo una edad de" + edad

print (fullname)
  


text = "hola como estas"
nombre = input("ingrese su nombre")


fulltext = text + nombre
fulltextv1 = f"{text} {nombre} ..!"
print(fulltext)
print(fulltextv1)"""



cadena = "Isaac no ronca así"
cadena_limpia = remover_caracteres_especiales(cadena)
es_palindromo = palindromo(cadena_limpia)
if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
es_palindromo = palindromo_recursivo(cadena_limpia, 0, len(cadena_limpia) - 1)
if es_palindromo:
    print("Con recursividad: es palíndromo")
else:
    print("Con recursividad: no es palíndromo")