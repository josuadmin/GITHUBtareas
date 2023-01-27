text = "Mi lenguaje favorito es python"
print("python" in text)

#Slicing 

print(text[0])
print(len(text))

size = len(text)
print(text[size - 1])


print(text[0:11])
print(text[3:])
print(text[:: -1])


#haciendo la correccion utilizando el comando "randome".


import random

my_randome= ["piedra", "papel", "tijera"]
computer = random.choice(my_randome).lower()
useropcion= input ("ingrese piedra papel o tijera: ").lower()


if computer == "piedra" and computer =="papel":
    print("Gano,papel a piedra ")
elif computer == "papel" and useropcion == "tijera!":
    print("Gano,tijera a papel ")
elif computer == "tijera" and useropcion == "piedra":
    print("Gano,piedra a tijera ")
if computer =="papel" and useropcion =="piedra":
    print("perdiste,La computadora gana papel a piedra")
elif computer == "tijera" and useropcion == "papel":
    print("perdiste,la computadora gana tijera a papel")
elif computer == "piedra" and useropcion == "tijera":
    print("perdiste,computadora gana piedra a tijera")
elif computer == useropcion:
    print("empate")




#explicacion.
numbar = 1;
numbers = [1,2,3,4,5]
fruits = ["pera", "manzana"]
tipos = [1, "banana", 2]

#ejercicio, tambien aplicando el comando "randome y choice".


import random



numbers = [1,2,3,4,5]

fruits = ["manzana", "pera", "banana"]

new_list = numbers + fruits



numbers[0] = "banana"

index = numbers.index(3)


numbers[index] = "change"



numbers.append(700)
numbers.insert(3,0)

print(numbers)
print(random.choice(fruits))


print("mi primer arreglo =>", numbers)
numbers.pop()
numbers.remove(2)

my_randome = random.choice(fruits)
print(random.choice(fruits))


#ciclos 

#while => es un ciclo infinito
#for => es un ciclo normal

count = 0 
 
while count < 10:
    count +=1
    print("10 veces")


while count < 100:
    count +=1
    print(count)




#ejercicio numero 7 "descuentos", de la hoja de pyhton de la semana 1.

import os

cantidad = float (input ('Ingresa el valor de cantidad: '))
pago = float (input ('Ingresa el valor de pago: '))
precio = float (input ('Ingresa el valor de precio: '))
importe=precio*cantidad
if cantidad>=100:
    descuento=importe*0.20
else:
    descuento=0
importetot=importe-descuento
cambio=pago-importetot
print ('Valor de cambio: ' + repr (cambio))
print ('Valor de descuento: ' + repr (descuento))
print ('Valor de importe: ' + repr (importe))
print ('Valor de importetot: ' + repr (importetot))
print ()
os.system ('pause')










