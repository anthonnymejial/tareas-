
alumno={ "1105050775":"veronica chimbo",
         "0107050270":"anthonny mejia",
         "0106399041":"jacquiline tenesaca",
         "0106663798":"juan bravo",
         "1105050775":"Veronica Chimbo",
         "1501095408":"Pizango Jhordan",
         "0105410211":"Christian Preciado",
         "0106605017":"Astudillo Carlos",
         "0106767007":"Bruce",
         "0105737365":"Stallin Barbecho",
         "0954337572":"Torres melanie",
         "0106637150":"Paredes Jennifer",
         "0150564078":"Danny Alex",
         "0105041982":"Adrian Piña",
         "0150474021":"David Ñauta",
         "0107270282":"Edwin Arroyo",
         "0107359788":"ariel villa",
    
}

print(alumno)
#accede
print(alumno,["0150564078"])
print(alumno.get,("0150564078","no se encuentra"))
#eliminar
alumno.pop("0954337572")
print(alumno)
print(alumno.get("09543337572"))
#
# llaves
print(alumno)