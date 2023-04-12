print ("Nombre:anthonny mejia")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
numero= input ("ingrese un numero:")
if len(numero) != 1:
    print("no se puede procesar el dato. debe ingresar un numero.")
elif numero in "0123456789":
    print("es numero",numero)
else:
    print("no es numero",numero)