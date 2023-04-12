print ("Nombre:anthonny mejia")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
frase = input("Introduce una frase: ").lower().replace(" ", "")

if frase == frase[::-1]:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
