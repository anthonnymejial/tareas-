instituto={
    "carreras":["cyberseguridad","mecatronica","bigdata","desarrollode software","mecatronica","infrestructita"],
    "materias":["arquitecturade coputadoras","lenguage","metodologia","redes de datos","sistemasoperativos","soporte de hartwaare","laboratorio"],
    "profesores":["monica","william","adriana","belen","ana","hasn"],
    "notas":[70,70,75,78,83,85,80],
          }
print(instituto["carreras"])
print(instituto["materias"])
print(instituto["profesores"])
print(instituto["notas"])

#
no=0
for e in instituto["notas"]:
    no+=float(e)
print(no/len(instituto["notas"]))


#
nu=sum(instituto["notas"])/len(instituto["notas"])

#
print(sum(instituto["notas"])/len(instituto["notas"]))
#
suma=0
for e in instituto["notas"]:
    suma+=e
print(suma/len(instituto["notas"]))
print(round(suma/len(instituto["notas"]),2))
#max
print(max(instituto["notas"]))
#min
print(min(instituto["notas"]))
#ejercicio
minima=70
print(min(instituto["notas"]))
posicion=instituto["notas"].index(minima)
print("nota mas baja",posicion)
#
notaminima=min(instituto["notas"])
posicion=instituto["notas"].index(notaminima)
print("la nota minima es:",notaminima)
print("la materiaes:",instituto["materias"][posicion])
print("los proferosres son:",instituto["profesores"][posicion])



    
