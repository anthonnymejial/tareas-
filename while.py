
def saludo():
    #def num1+num2
    #retur num1+num2
    print("hola ususario")
def formateo(nombre, apellido):
    print(nombre, apellido)
bandera =True
while bandera :
    print("menu de opciones")
    print("1 suma")
    print("2 resta")
    print("3 multiplicasion")
    print("4 division")
    print("5 saludo")
    print("6 formateo")
    print("7 es salida")
    opcion=int(input("ingrese un valor"))
    if opcion!=5:
        num1=int(input("ingresa numero 1"))
        num2=int(input("ingresa numero 2"))
        if opcion==1:
            print("la suma",sum(num1+num2))
        elif opcion==2:
            print("la resta",num1-num2)
            #print("la resta",rest(num1-num2))
        elif opcion==3:
            print("la multiplicasion",num1*num2)
          #  print("la multiplicasion",num1*num2)
            
        elif opcion==4:  
            print("la division",num1/num2)
        elif opcion==5:
            saludo()      
        elif opcion==6:  
            
        else:
            bandera=False
            print("fin de ciclo")
            print("nueva linea")
            
            
            
            
        
    