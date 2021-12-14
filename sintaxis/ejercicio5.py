class Calculadora:
    def __init__(self, numero1, numero2):
          self.num1 = numero1
          self.num2 = numero2
    def suma(self):
         return self.num1 + self.num2
    def resta(self):
         pass
    def mutiplicacion(self):
        multi = self.num1*self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))
    def división(self):
         pass
     
class CalEstandar(Calculadora):
    def __init__(self, nume1, nume2):
           super().__init__(nume1,nume2)
           
    def mutiplicacion(self):
        return self.num1*self.num2
    def exponente(self):
         pass
    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        return numero
     
class CalCientifica(Calculadora):
    def __init__(self, numero1, numero2):
           super().__init__(numero1,numero2)
    
    def  circunferencia(radio):
        print("circunferencia")
           
# cal =Calculadora(5,8)  
# print(cal.suma())
# cal.mutiplicacion()
  
# est = CalEstandar(4,6)
# print(est.suma())
# print(est.mutiplicacion())
# print(est.valorAbsoluto(-5))
  