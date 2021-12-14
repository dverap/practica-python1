
class Menu:
     def __init__(self,tit,opc):
         self.titulo=tit
         self.opciones=opc
     
     def menu(self):
         print(self.titulo)
         for opcion in self.opciones:
             print(opcion)
         opc = input("Elija opcion[1...{}]: ".format(len(self.opciones)))
         return opc    
     
