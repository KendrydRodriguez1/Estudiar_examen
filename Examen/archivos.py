#Crear y sobre escribir (w)
#Para leer (r)
#Para escribir más (a)
print("----------")
from pathlib import Path
archivo_1 = Path("./archivo1.txt")
with archivo_1.open( mode="w") as file_1:
    file_1.write("hola\nsalto de linea-\n")
    file_1.write("me  hola   bro")
    
    
    
#Leer (abrir y leer)
with open("./archivo1.txt", "r") as file:
    for i in file:
        print(i)
print("-------------")

  
#Verificar si exiate y saca la ruta padre
from pathlib import Path
archivo = Path("./archivo.text")
print(archivo.parent)
print("-----------")


#Nombre del archivo
print(archivo.name)
print("----------------")


#Sacar la ruta
print(archivo.absolute())
print("----------------------")


#Contar linea de txt
print("Comenzar")
x = 0
y = 0


#Contar lineas  
with archivo_1.open( mode="r") as file_1:
    for i in file_1:
      x += 1
print(x)
print("--------------")


#Contar caracteres
with open("archivo1.txt", "r") as file_1:
    texto = file_1.read()
    texto = texto.replace("\n", "").replace(" ", "")
    print(len(texto))
print("---------------")


#Contar palabras
x = 0
with open("./archivo1.txt", "r") as file_1:
    texto = file_1.read().replace("\n", " ")
    texto = texto.split(" ")
    while "" in texto:
        texto.remove("")
    print(len(texto))
print("------------")


#cambiar caracter
with open("./archivo1.txt", "r") as archivo:
    texto = archivo.read()
    if "hola" in texto:
        texto = texto.replace("hola", "me")
    print(texto)
with open("./archivo1.txt", "w") as archivo:
    archivo.write(texto)
print("----------")


#Contar cuantas veces aparece una palabra
x = 0
with open("./archivo1.txt", "r") as archivo:
    texto = archivo.read().replace("\n", " ")
    texto = texto.split(" ")
    for i in texto:
        if "me" == i:
            x +=1
    print(x)
print("-------------")


#Eliminar lineas
with open("./entrada.txt", "r") as archivo, open("./salida.txt", "w") as salida:
    for i in archivo:
        if i.strip():
            salida.write(i)
with open("./salida.txt", "r") as salida:
    text = salida.read()
    print(text)


print("------------------------")
#Sumar numero par
x = 0
with open("./numeros.txt", "r") as file:
    numer = file.read()
    numer = numer.split(" ")
    for i in numer:
        try:
            i = int(i)
            if i % 2 == 0:
                x += i
        except:
            print("El numero que ingreso no es un numero entero")
    print(x)


print("------------------")
#Contar palabras distintas
x = []
y = 0
with open("./entrada.txt", "r") as file:
    text = file.read().replace("\n", " ")
    text = text.split(" ")
    while "" in text:
        text.remove("")
    for i in text:
        if i not in x:
            x.append(i)
            y += 1
    print(y)
print("---------------")


#Ordena mediante el abecedario palabras
with open("./alfabeticamente.txt", "r") as file:
    text = file.read()
    text = text.replace("\n", " ")
    text = text.split(" ")
    text.sort()
    resultado = " ".join(text)
    print(resultado)

#Palabras mas largar a la mas corta
print("-----------")
palabras = []
with open("./palabras_largas.txt", "r") as file:
    text = file.read().replace("\n", " ")
    text = text.split()
    final = sorted(text, key=lambda x:len(x), reverse=True)
    print(final)
    

            
    
            
                
    
    
    