import os
from datetime import date
from abc import ABC,abstractmethod

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")
    
class Empresa:
    def __init__(self, razonSocial, direccion, telefono, ruc):
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc
       
    def mostrarEmpresa(self):   
        print(''' {} 
        - Ruc : {} 
        - Dirección : {} 
        - Teléfono: {}'''.format(self.razonSocial,self.ruc, 
                                     self.direccion, self.telefono))
       
class Departamento:
    codigo = 0
    def __init__(self, descripcion):
        Departamento.codigo += 1
        self.__id = Departamento.codigo
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def mostrarDepartamento(self):
        print('{}. DEPARTAMENTO DE {}'.format(self.id,self.descripcion))
        print(' ')
class Cargo:
    codigo = 0
    def __init__(self, descripcion):
        Cargo.codigo += 1
        self.__id = Departamento.codigo
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def mostrarCargo(self):
        print('{}. CARGO {}'.format(self.id,self.descripcion))
        print(' ')
    
class Empleado(ABC): 
    codigo = 0
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo):
        Empleado.codigo += 1
        self.__id = Empleado.codigo
        self.nombre = nombre
        self.departamento=departamento
        self.cargo = cargo
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fechaIngreso = fechaIngreso
        self.sueldo = sueldo

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def valorHora(self):  
        return self.sueldo/240
    

    def mostrarEmpleado(self):
        print(' {} Empleado : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")



class Admistrativo(Empleado):
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,comision= True):
        super().__init__(nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo)
        self.comision = comision

   
    def mostrarEmpleado(self): 
        print(' {} Administrativo : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")
        print("Comision:{}".format(self.comision))

    def valorHora(self):
        return super().valorHora()
    
class Obrero(Empleado):
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo, cc= True):
        super().__init__(nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo)
        self.cc = cc

   
    def mostrarEmpleado(self): 
        print(' {} Obrero : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")
        print("CColectivo:{}".format(self.cc))

    def valorHora(self):
        return super().valorHora()
         
class Deduccion:
    def __init__(self, iess, comision, antiguedad):
        self.__iess = iess
        self.__comision = comision
        self.__antiguedad = antiguedad
      
    def iess(self):
        return round(self.__iess/100,4)
    
    def comision(self):
        return round(self.__comision/100,2)
    
    def antiguedad(self):
        return round(self.__antiguedad/100,2)
    
    def mostrarDeduccion(self):
        print('Valor Iess {} = \n Valor comision ({}) = \n Valor antiguedad ({}) ='.format(self.iess, self.comision, self.antiguedad))

class Prestamo:
    codigo = 0
    def __init__(self,empleado, aamm, valor, numPagos,saldo, estado= True):  #!Falta la relacion con empleado
        Prestamo.codigo += 1
        self.__id = Prestamo.codigo
        self.empleado=empleado
        self.aamm = aamm
        self.valor = valor
        self.numPagos = numPagos
        self.cuota = valor/numPagos
        self.saldo = saldo
        self.estado = estado

    @property
    def id(self):
        return self.__id

    def mostrarPrestamo(self):
        print('''{}° Prestamo realizado: {}
          - Empleado= {}
          - Valor = ${}
          - Numeros Pagos = {}  
          - Cuota = ${:.2f} 
          - Saldo = ${:.2f}
          - estado = {} '''.format(self.id,self.aamm,self.empleado.nombre,self.valor,self.numPagos,self.cuota,self.saldo,self.estado))
        
class Sobretiempo:
    codigo = 0
    def __init__(self,empleado, aamm,hSuplementarias,hExtraordinarias,estado= True): 
        Sobretiempo.codigo += 1
        self.__id = Sobretiempo.codigo
        self.empleado=empleado
        self.aamm = aamm
        self.h50 = hSuplementarias
        self.h100 = hExtraordinarias
        self.estado = estado

    @property
    def id(self):
        return self.__id

    def sobretiempo(self):
        return round(self.empleado.valorHora()+(self.h50*1.5+self.h100*2),2)
    
    def mostrarSobretiempo(self):
        print('''{}° Sobretiempo realizado: {}
          - Empleado= {}
          - H50 = {}
          - H100 = {}  
          - Valor = ${:.2f} 
          - estado = {} '''.format(self.id,self.aamm,self.empleado.nombre,self.h50,self.h100,self.sobretiempo(),self.estado))
        
class CalculoRol(ABC):
    @abstractmethod
    def getSueldo(self):
        pass
    @abstractmethod
    def getSobretiempo(self):
        pass
    @abstractmethod
    def getComision(self):
        pass
    @abstractmethod
    def getAntiguedad(self):
        pass
    @abstractmethod
    def getIess(self):
        pass
    @abstractmethod
    def getPrestamo(self):
        pass 
    
class Nomina:
    secuencia = 0
    def __init__(self,fecha,aamm, tipoRol):
        Nomina.secuencia += 1
        self.__id = Nomina.secuencia
        self.fecha = fecha
        self.aamm = aamm
        self.rol = tipoRol
        self.totIngresos=0
        self.totDescuentos=0
        self.totPagoNeto=0
        self.canEmp = 0
        self.detalleNomina = []
        
    @property
    def id(self):
        return self.__id

    def calcularNominaDetalle(self,empleado):
        detalle = DetalleNomima(empleado)
        rubrosIngresos = detalle.calcularRubrosIngresos()
        rubrosEgresos = detalle.calcularRubrosEgresos()
        self.totIngresos += detalle.totIng
        self.totDescuentos += detalle.totDes
        self.totPagoNeto += detalle.totLiq
        self.detalleNomina.append([[empleado],rubrosIngresos,rubrosEgresos])        
        
    def mostrarCabeceraNomina(self,razonSocial, direccion, telefono, ruc):
        os.system('cls')
        print('              {} Ruc : {} Teléfono : {} Dirección: {}'.format(razonSocial,ruc,telefono,direccion))
        print('--------------------------------------------------------------------------------------------------------------------')
        print('FECHA: {}  N O M I N A   D E   P A G O  D E   E M P LE A D O S: {}  '.format(self.fecha,self.rol))
        print('Nomina#:{}  Correspondiente al Periodo:{}'.format(self.id,self.aamm))
        print('--'*59) 
        print(" "*5,"E M P L E A D O S"," "*30,"I N G R E S O S"," "*22,"E G R E S O S")
        print("Nombre     Cargo          Departamento    Sueldo   Sobretiempo  Antiguedad  Comision TotIng   Iess    Prestamo   TotDes   Neto")
  
    def mostrarDetalleNomina(self):
        fila = 8
        for det in nomina.detalleNomina:
            emp = det[0][0]
            ing = det[1]
            des = det[2]
            #print(emp.nombre,emp.cargo.descripcion,emp.departamento.descripcion,ing[0],ing[1],ing[2],ing[3],des[0],des[1])    
            gotoxy(1,fila);print(emp.nombre,end="")    
            gotoxy(10,fila);print(emp.cargo.descripcion,end="")    
            gotoxy(25,fila);print(emp.departamento.descripcion,end="")    
            gotoxy(43,fila);print(ing[0],end="")    
            gotoxy(53,fila);print(ing[1],end="")    
            gotoxy(67,fila);print(ing[2],end="")    
            gotoxy(78,fila);print(ing[3],end="")    
            gotoxy(86,fila);print(ing[4],end="")    
            gotoxy(95,fila);print(des[0],end="")    
            gotoxy(104,fila);print(des[1],end="")    
            gotoxy(114,fila);print(des[2],end="")    
            gotoxy(122,fila);print(des[3],end="")    
            fila+=1
        
class DetalleNomima(CalculoRol):
    secuencia = 0
    def __init__(self,empleado):
        DetalleNomima.secuencia += 1
        self.__id = DetalleNomima.secuencia
        self.empleado = empleado
        self.totIng=0
        self.totDes=0
        self.totLiq=0
       
    def getSueldo(self):
        return self.empleado.sueldo
    
    def getSobretiempo(self):
        return sob1.sobretiempo()
    
    def getAntiguedad(self):
        return round(self.empleado.valorHora()*ded.antiguedad(),2)
    
    def getComision(self):
        return round(self.empleado.valorHora()*ded.comision(),2)
    
    def getIess(self):
        return round(self.empleado.sueldo*ded.iess(),2)
        
    def getPrestamo(self):
        return round(prest1.cuota,2)
    
    def calcularRubrosIngresos(self):
        ingresos = []
        ingresos.append(self.getSueldo())
        ingresos.append(self.getSobretiempo())
        ingresos.append(self.getAntiguedad())
        ingresos.append(self.getComision())
        for valor in ingresos:
            self.totIng += valor
        ingresos.append(self.totIng)    
        return ingresos
  
    def calcularRubrosEgresos(self):
        descuentos = []
        descuentos.append(self.getIess())
        descuentos.append(self.getPrestamo())
        for valor in descuentos:
            self.totDes += valor
        self.totLiq = round(self.totIng - self.totDes,2)
        descuentos.append(self.totDes)    
        descuentos.append(self.totLiq)    
        return descuentos
  
    
os.system('cls')
emp = Empresa('EMPRESA XYZ','Milagro','0999999999','042435567') 
#emp.mostrarEmpresa()
dep = Departamento('Informatica')
#dep.mostrarDepartamento()
car = Cargo("Programador")
#car.mostrarCargo()
#emp = Empleado("Daniel",dep,car,"Milagro",'0914192182','0992269847',date(1969,5,21),1000)
#emp.mostrarEmpleado()
empAdm1 = Admistrativo("Daniel",dep,car,"Milagro",'0914192182','0992269847',date(1969,5,21),1000,True)
empAdm2 = Admistrativo("Erick",dep,car,"Milagro",'0914192182','0992269847',date(2018,5,21),2000,True)
#empAdm.mostrarEmpleado()
empObr1 = Obrero("Jose",dep,car,"Milagro",'0914192182','0992269847',date(1980,5,21),500)
empObr2 = Obrero("Manuel",dep,car,"Milagro",'0914192182','0992269847',date(1990,5,21),600)
empleados = [empAdm1,empAdm2]
obreros = [empObr1,empObr2]
#empObr.mostrarEmpleado()
ded = Deduccion(9.35,5,2)
#print(ded.iess())
prest1 = Prestamo(empAdm1,'202109',500,5,500)
prest2 = Prestamo(empAdm2,'202109',600,3,600)
#prest.mostrarPrestamo()
sob1 = Sobretiempo(empAdm1,'202109',20,10)
sob2 = Sobretiempo(empAdm2,'202109',10,5)
#sob.mostrarSobretiempo()
nomina = Nomina(date.today(),'202109',"O B R E R O S")
for empleado in obreros:
    #print(emp.nombre,emp.cargo.descripcion)
    nomina.calcularNominaDetalle(empleado)
    
nomina.mostrarCabeceraNomina(emp.razonSocial,emp.direccion,emp.telefono,emp.ruc)
nomina.mostrarDetalleNomina()


                                                      
    



