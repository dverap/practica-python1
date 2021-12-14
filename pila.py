class Stack:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]
        
    def presentar(self):
        return self.items[len(self.items)-1]  
    
    def push(self, valor):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(valor)    
    
    def pop(self):
       if self.es_vacia():
          return None
       else:
          elemento = self.items[-1]
          self.items = self.items[:-1]
          return elemento
        
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []    
    
pila = Stack()
nombre = "Jessica"
pila.push(nombre)
print(pila.presentar())
dato=pila.pop()
pila.push("Tanya")
pila.push("Liz")
print(pila.presentar())
pila.push("Margoth")
pila.push(dato)    
print(pila.presentar())  
pila.pop()
pila.pop()
print(pila.presentar())  
Jessica,Liz,Jessica,Liz