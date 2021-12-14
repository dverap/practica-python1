class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def quitar(self):
        return self.items.pop()
    
    def presentar(self):
        print(self.items[len(self.items)-1])
    
cola = Cola()
cola.agregar("Ana")    
cola.agregar("Jose")
nombre= cola.quitar()
cola.quitar()
cola.agregar(nombre)
cola.agregar("Erick")
cola.presentar()
    