class PilaEstatica:
    def __init__(self,tamanio):
        self.__lista=[]
        self.__tope = 0
        self.__size = tamanio
    
    def push(self,dato):
        if self.__tope < self.__size:
            self.__lista = self.__lista + [dato]
            self.__tope += 1
        else:
            print("La Pila esta llena")
                    
    def empty(self):
        if self.__tope == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.__lista[-1]
            self.__lista = self.__lista[:-1]
            self.__tope -= 1
            return top
          
    def show(self):
        for tope in  range(self.__tope-1,-1,-1):
            print("[{}]".format(self.__lista[tope]))
        
    def longitud(self):
         return self.__tope
     
# pila = PilaEstatica(4)
# pila.push(3)
# pila.push(2)
# pila.push(1)
# print(pila.pop())
# pila.show()