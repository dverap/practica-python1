def menu(opciones,titulo):
    print('{} {} {}'.format("*"*int(len(titulo)/2),titulo,"*"*int(len(titulo)/2)))
    for op in range(0, len(opciones)):
        print('{}){}'.format(op+1,opciones[op]))
    opc = int(input('Elija opcion[1...{}]'.format(len(opciones))))
    return opc

menu(["Ingresar","modificar","salir"],"Menu Ejercicios")