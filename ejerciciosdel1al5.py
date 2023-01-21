#aqui el primer ejercicio, numero par o inpar.

number_opcion = int(input("ingrese un numero"))

if number_opcion % 2 == 0:
    print("el numero:", number_opcion,", si es par")
else: 
    print("el numero:", number_opcion,", no es par")


#aqui el segundo ejercicio, numero mayor.

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese en segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))

if n2 < n1 > n3:
    print("el numero mayor es:", n1)

if n1 < n2 > n3:
    print("el numero mayor es:", n2)

if n1 < n3 > n2:
    print("el numero mayor es:", n3)


#aqui el tercer ejercicio, ordenacion de tres numeros.

n1 = int(input("ingrese el primer numero: \n"))
n2 = int(input("ingrese en segundo numero: \n"))
n3 = int(input("ingrese el tercer numero: \n"))

if n2 < n1 > n3:
    print("el numero mayor es:", n1,"el numero del medio es:", n2,"el numero menor es:", n3)

if n1 < n2 > n3:
    print("el numero mayor es:", n2,"el numero del medio es:", n1,"el numero menor es:", n3)

if n1 < n3 > n2:
    print("el numero mayor es:", n3,"el numero del medio es:", n2,"el numero menor es:", n1)


#aqui el cuarto ejercicio, numero es multiplo de otro.

n1 = int(input("ingrese el numero base: "))
n2 = int(input("ingrese el multiplo: "))

m = int(n2 % n1)

if m == 0:
    print("el numero es multiplo")
else:
    print("el numero no es multiplo")


#aqui el quinto ejercicio, año bisiesto.

annio = int(input("ingresa un año:"))

if (annio % 4 == 0 and annio % 100 != 0) or annio % 400 == 0:
    print("el año:",annio,",es bisiesto")
else:
    print("el año:",annio,",no es bisiesto")

