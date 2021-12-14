class Pila:
    def __init__(self,tamanio):
        self.__lista = [] 
        self.__tope =0
        self.size=tamanio

    def empty(self):
        return self.__tope == 0
    
    def push(self,dato):
        if self.__tope < self.size:
            self.__lista = self.__lista + [dato]
            self.__tope += 1
        else:
            print("La lista esta LLena")
                
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.__lista[-1]
            self.__tope -= 1
            self.__lista = self.__lista[:-1]
            return top
    
    def show(self):
            print("{}".format(self.__lista[self.__tope-1]))
        
    def longitud(self):
        return self.__tope   
    
pila = Pila(10)  
pila.push(4)    
pila.push(6)    
x=pila.pop()
y=pila.pop()
pila.push(7)
pila.push(y)
pila.push(x)
pila.pop()
pila.show()

# print(pila.pop())
# pila.show()
# print(pila.pop())
# pila.show()
# print(pila.pop())
# pila.show()
