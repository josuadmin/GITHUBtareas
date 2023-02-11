# tuplas

option = ('piedra', 'papel', 'tijera');

# metodos propios de las tuplas

print(option.count('piedra'))
print(option.index('piedra'))

# option[0] = 'bomba' => no se puede realizar 
optionv1 = list(option)
optionv1[0] = 'bomba'

print(option[0])
print(optionv1[0])
print(type(option))















