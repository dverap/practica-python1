# num1 = 20
# num2 = 10


# def suma():
#     sumar = num1+num2
#     print("Suma:{}+{}={}".format(num1,num2,sumar))

# def multiplicacion():
#     nume1=4
#     nume2=3
#     print("{}*{}={}".format(nume1,nume2,nume1*nume2))

# def resta(n1,n2):
#     restar = n1-n2
#     print("Resta:",n1,"-",n2,"=",restar)
# suma()
# numero1 = int(input("Ingrese numero1: "))
# numero2 = input("Ingrese numero2: ")
# numero2 = int(numero2)
# resta(numero1,numero2)
# multiplicacion()


class Operacion:
    
    def __init__(self):
        self.num1=20
        self.num2=10
    
    def suma(self):
        sumar = self.num1+self.num2
        print("Suma:{}+{}={}".format(self.num1,self.num2,sumar))

    def multiplicacion(self):
        nume1=4
        nume2=3
        print("{}*{}={}".format(nume1,nume2,nume1*nume2))

    def resta(self,n1,n2):
        restar = n1-n2
        print("Resta:",n1,"-",n2,"=",restar)
        
ope = Operacion()        
ope.resta(2,1)  
ope1 = Operacion()        
ope1.resta(5,3)  
ope2 = Operacion()        
ope2.resta(4,2)  
  
clientes = [{"nombre":"Dan","Pago":100,"costo":70},{"nombre":"Ana","Pago":200,"costo":40},{"nombre":"Josue","Pago":200,"costo":60}]
                          #    0                                     1
lista = [2,4,6,8,10]
     #    0 1 2 3  4 
nombres = ["ana","dan","juan"]
      #       0     1     2
print(lista[1],clientes[1]["nombre"],nombres[1])                      
# def vuelto(clientes):
#     for cliente in clientes:
#         vuelto = cliente["Pago"] - cliente["costo"]
#         print(cliente["nombre"],vuelto)
# vuelto(clientes)
          
  
       

    

    