# Tenemos una lista de Tuplas que representan ciertas características de una serie de productos.
# Cada tupla tiene 4 elementos:
# nombre del producto
# precio
# cantidad disponible
# marca
# Se desea obtener una lista de productos que cumplan con ciertas condiciones de búsqueda:
# precio máximo
# marca específica

productos = [("remera", 5.000, 5, "nike"), ("pantalon", 8.500, 3, "af jean"), ("buzo", 12.000, 10, "adidad"), ("campera", 30.000, 2, "puma")]

precio_maximo = 12.000
marca_buscada = "nike"
productos_filtrados = []

for producto in productos:
    if producto[1] <= precio_maximo and producto[3] == marca_buscada:
        productos_filtrados.append(producto)
print(productos_filtrados)

# Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
# longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
# error.
# El programa termina cuando el usuario introduce un cero.

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if 1 <= numero <= len(meses):
        mes = meses[numero - 1]
        print("El mes correspondiente es:", mes)
    else:
        print("Error: número fuera de rango.")

# Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
# repite según lo halle en la tupla que has creado.
# RESUELVE validar los ingresos del usuario.

numeros = (1, 5, 8, 4, 6, 3, 10, 2)

while True:
    try:
        numero_usuario = int(input("Ingresa un número: "))
        break  
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

repeticiones = numeros.count(numero_usuario)
print("El número", numero_usuario, "se repite", repeticiones, "veces en la tupla.")

# Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.

numeros = (5, 10, 2, 8, 3, 1, 9, 7)

maximo = max(numeros)
minimo = min(numeros)

print("El número con el mayor valor es:", maximo)
print("El número con el menor valor es:", minimo)

# Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y
# muestra los valores de la tupla.

# RESUELVE el caso en que no exista ese índice en la tupla.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num=int(input("Ingrese un numero del 1 al 9:"))

if num >= 0 and num < len(tupla):
    valor = tupla[num]
    
    print("El valor en el índice", num, "es:", valor)
else:
    print("Error: El índice está fuera del rango de la tupla.")
    