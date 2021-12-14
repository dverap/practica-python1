class Ambito:
    pi = 3.1416
    def __init__(self,n1=0,n2=0):
        self.num1=n1
        self.num2=n2
        
    def mayor(self):
      
        if self.num1 > self.num2:
            print(self.num1)
        else:
            print(self.num2)
    
    def area(self,radio):
          radio = radio**2
          area = Ambito.pi*radio
          print("radio metodo",radio)
          return area
      
# numero1 = 20
# numero2= 10
# ejer1 = Ambito(numero1,numero2)
# ejer1.mayor()
ejer2 = Ambito()
ejer2.mayor()
radio = 4
print(ejer2.area(radio))
print("radio Principal",radio)
