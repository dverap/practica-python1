class Lista:
    def __init__(self):
        self.lista = []
   
    
    def eliminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
            return None
        else:
            valor = self.lista[pos]
            listaAux = self.lista[0:pos+1] 
            for indice in range(pos,len(self.lista)):
                listaAux = listaAux + [self.lista[indice]] 
            self.lista = listaAux
            return valor
       
    def mostrar(self):
         for pos in range(len(self.lista)):
                print("[{}]".format(self.lista[pos]))
                

lista1 = Lista()
lista1.lista.append(10) 
lista1.lista.append(20) 
print(lista1.eliminarElemento(1))


    

        