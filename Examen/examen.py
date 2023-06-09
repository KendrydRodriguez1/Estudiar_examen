
lista = [2,3,4,5,6,7]
x = 0
y = 0
for i in lista:
    if i % 2 == 0:
        x += 1
    else:
        y += 1
print(f"Los nuumero pares son: {x}")
print(f"Los numeros impares son: {y}")


print("Inversa de una lista")
lista = ["hola", 2, 4, "me"]
lista.reverse()
print(lista)



print("-----------------")
lista = []
numero = int(input("Ingrese la cantidad de numero que desea ingresar: "))
x = 0
while x < numero:
    dato = input("Ingrese un numero: ")
    try:
        int(dato)
        lista.append(int(dato)) 
    except:
        print("Ah ingresado un valor que no es numerico")
    x += 1
print("Desendente")
lista.sort()
lista.reverse()
print(lista)

print("-------------")
print("Ascendente")
lista.sort()
print(lista)

print("-------------------------")
print("Buscar un elemnto dentro de una lista")
lista = ["hola", 3 , 4, 5, 7, 8]
dato = input("Ingrese el elemento que quiera buscar dentro de una lista")
dato = dato.strip(" ")
print(dato)
if dato in lista:
    dato = dato.index(dato)
    print(f"Se ha encontrado el elemento y esta en la posicion {dato}")





