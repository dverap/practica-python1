class Condicion:
    
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
        numero = 10
        self.numero3=numero

    def Condicion(self):
        # if ... elif ... else ...: permiten condicionar la ejecución de uno o varios bloques
        # de sentencias al cumplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("{} y {} son iguales".format(self.numero1,self.numero2))
        elif  self.numero1 < self.numero3:
            print("{} es menor a {}".format(self.numero1,self.numero3))
        else:
            print("no son iguales")
        # operador ternario
        print(self.numero1,"Es entero") if type(self.numero1) == int else print(self.numero1,"es ",type(self.numero1))

condi1 = Condicion(8.5,18)
print(condi1.numero1,condi1.numero2,condi1.numero3)
condi1.Condicion()


