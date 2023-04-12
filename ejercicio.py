dias = int(input("Ingrese la cantidad de días: "))

# Calcular la cantidad de horas, minutos y segundos en la cantidad de días
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

# Mostrar el resultado por pantalla
print("En", dias, "días hay", horas, "horas,", minutos, "minutos y", segundos, "segundos.")