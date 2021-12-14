import os
class Nota:
    def __init__(self,nombre,materia,n1,n2):
        self.nombre=nombre
        self.materia=materia
        self.nota1=n1
        self.nota2=n2
        self.promedio = n1+n2
        self.obs = "Aprobado" if self.promedio >=70 else "Reprobado"
        self.notas = []
        
    def mostrar(self):
       return "{:7} {:12} {:2} {:6} {:8} {}". \
              format(self.nombre,self.materia,self.nota1,self.nota2,self.promedio,self.obs)
 
notas = []
estudiante1 = Nota("Daniel","POO",40,50)              
estudiante2 = Nota("Yady","POO",40,40)              
estudiante3 = estudiante1 #Nota("Erick","Estructura",50,50)
estudiante3.nombre="Erick"              
estudiante4 = Nota("Romina","Construccion",20,40)
notas.append(estudiante1)              
notas.append(estudiante2)              
notas.append(estudiante3)              
notas.append(estudiante4)
os.system("cls")
print("Listado de Notas de Estudiante UNEMI")
print("Nombre  Materia   Nota1  Nota2  Promedio Observacion")
for nota in notas:
    print(nota.mostrar())              
