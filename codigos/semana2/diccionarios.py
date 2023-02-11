# diccionarios

services = {
    'id' : 1,
    'name' : 'desarrollo de app',
    'precio' : '400',
    'tool' : ['lapto' , 'servidores' , 'pizarra digital']
}

print('id' in services)
services['id'] = 2

services.pop('id')


#print(services.items())
#print(services.keys())
#print(services.values())

print(services['tool'][1])

print(services['name'])