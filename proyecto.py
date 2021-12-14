from menus import Menu
from calculadora import CalEstandar,CalCientifica

import os
opcion=""
while opcion !="5":
    men = Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Cadenas","5) Salir"])
    opcion = men.menu()
    os.system ("cls") 
    if opcion == "1":
        opc1=""
        while opc1 !="3":
            os.system ("cls")  
            men = Menu("Menu Calculadora",["1) Suma","2) Resta","3) Salir"])
            opc1 = men.menu()
            os.system ("cls")  
            if opc1 == "1":
                print("Suma de dos Numeros")
                n1 = int(input("Ingrese numero1: "))
                n2 = int(input("Ingrese numero2: "))
                est = CalEstandar(n1,n2)
                print("{}+{}={}".format(n1,n2,est.suma()))
                input("presione una tecla para continuar...")
    elif opc1 == "2":
            print(6-2)
                
    elif opcion == "2":
        men = Menu("Menu Numeros",["1) Primo","2) Prefecto","3) Amigos","4) Salir"])
        opc2 = men.menu()  
    elif opcion == "3":
        print("Menu Listas")    
    elif opcion == "4":
        print("Menu Cadenas")    
    elif opcion == "5":
        print("Salir")    
    else:
        print("Opcion no Valida")    
 
print("Gracias por su vista")
 