num1 = 3;
num2 = 4;

res = num1 + num2
print(res)

def sum():
    print("hola esta es mi primera funcion")

sum();




# scopo

def sum(n,v, iva = 0.12):
    print(n+v+iva)

sum(3,4);






num1 = 10;
res = 0;
def increment(res):
    num1 = 20;
    res += 10
    return res, num1

#res_final = increment(res);
#res_finalicima = increment(res_final)
respuesta1, respuesta2 = increment(res)

print(respuesta2)