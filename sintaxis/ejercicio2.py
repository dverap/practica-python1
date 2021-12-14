class Logica:
    def __init__(self,dato):
        self.__lista=dato
        self.__estado=True
    
    def par(self,numero):
        rec = numero % 2
        return rec
    
    def sumaPares(self):
        acu=0
        for num in self.__lista:
            if self.par(num) == 0:
                acu=acu+num
        return acu
    
    def perfecto(self,numero):
        acu=0
        for divisor in range(1,numero): 
            rec = numero%divisor
            if rec == 0:
               acu=acu+divisor
        return acu
    
    def divisoresNumero(self,numero):
        divisores = []
        for divisor in range(1,numero): 
            rec = numero%divisor
            if rec == 0:
               divisores.append(divisor)
        return divisores


class Ejercicios(Logica):
    def __init__(self,numeros,valor):
        super().__init__(numeros)
        
    def suma(self,n1,n2):
        if super().par(n1)==0:
            return (n1+n2)*2
        else:
            return (n1+n2)
    def resta(self,n1,n2):
        return n1-n2
    
    def par(self,numero):
        rec = numero % 2
        if rec == 0:
            print(numero,"Es Par")
        else:    
            print(numero,"Es Impar")
    
ejer = Ejercicios([2,3,4],20)
print(ejer.par(4))
print(ejer.suma(4,2))
