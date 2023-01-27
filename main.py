nombre = input("ingrese su nombre")
apellido = input("ingrese el apellido")
edad = input("ingrese su edad")

fullname = "hola" + "mi nombre es" + nombre + "mi apellido es" + apellido + "y tengo una edad de" + edad

print (fullname)
  


text = "hola como estas"
nombre = input("ingrese su nombre")


fulltext = text + nombre
fulltextv1 = f"{text} {nombre} ..!"
print(fulltext)
print(fulltextv1)


print{text (0:4)}
print{text (9:9)}


number_opcion = int(input("ingrese un numero"))

if number_opcion % 2 == 0:
    print("el numero es par")
else: 
    print("el numero es inpar")



#como hacer lo de numeros primos.

def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return false 
    for x in range (2, int(numero/2)):
        if numero % x == 0:
           return false
        return true   
    
