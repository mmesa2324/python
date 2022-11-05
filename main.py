
def print_hi(name): #esto es una funcion
    #hdahd
    print(f'Hi, {name}')
    name = str('miguel')
    print(name)



if __name__ == '__main__':
    print_hi('PyCharm')

x = int(5)
print(x)

y = str('john')
print(y)

z = float(0.3)
print(z)

miCarro = str('mazda')

print(x, y, z)

carname = str('Volvo')
print(carname)

#casting
age = int(28)
name = str('miguel')
# ageStr = str(age)
print('Hi my name is ' + name + ' I am ' + str(age) + ' years old')

#Slicing
t = str('hola como estas?')
print(t[5:9])
# print(t.upper())
t = t.upper()
print(t)


#lists
perros = ['tr', 43, 0.1]
objetos = ['sombrilla', 'trapo', 'yate']
print(objetos[0])
print(objetos[-1])
print(objetos[1:3])
# validar si un elemento esta en la lista
if 'trapo' in objetos:
    print('si')
else:
    print('no esta')
#cambiar un elemento de la lista
objetos[2] = 'moto'
print(objetos)
# agregar un item a la lista
objetos.append('res')
print(objetos)
# insertar un item a la lista en la posicion deseada
objetos.insert(1, 'pato')
print(objetos)
# fusionar(extender) 2 listas
objetos2 = ['tren', 'avion']
objetos.extend(objetos2)
print(objetos)
#eliminar un item de la lista
objetos.remove('tren')
print(objetos)
# eliminar un item segun la posicion
objetos.pop(0)
print(objetos)
#eliminar la lista completa
# del objetos
# print(objetos[1])
# eliminar un item utilizando del
del objetos[1]
print(objetos)
# limpiar toda la lista con clear
# objetos.clear()
# print(objetos)

#loop en una lista
for objeto in objetos:
    print(objeto)