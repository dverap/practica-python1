class Busqueda:
    
    def __init__(self,listas=None):
        self.__lista=listas
           
    @property
    def lista(self):  # getProperty() retorna el valor de un atributo privado
        if self.__lista != None:
            return self.__lista
        else:
            print("Lista vacia")
    # busca un dato en una lista
    def buquedaBinaria(self,buscado):
        fin = len(self.lista)-1  
        inicio = 0 
        enc = False
        while inicio <= fin and enc==False:
            medio = (inicio+fin)//2
            if buscado == self.lista[medio]: enc= True
            elif buscado  < self.lista[medio]: fin = medio-1
            else: inicio = medio+1
        #return enc
 
        
        if enc: return (medio,inicio,fin)
        else: return (medio,inicio,fin)
    
    def  buquedaLineal(self,buscado):
        lon = len(self.__lista)
        enc=False
        pos=0
        # recorre la lista hasta que encontrar al dato buscado 
        # o pos sea igual a la longitud de la lista lo cual 
        # indica que el dato no fue encontrado
        while pos < lon and enc==False:
            if self.__lista[pos]["nombre"] == buscado: enc=True
            else: pos +=1     
        if enc: return pos
        else: return -1
        
    def ordenarQuickSort():
        pass
    
    def  ordenar(self,orden):
      if orden == "asc":  
        for pos in range(0,len(self.__lista)): 
           for sig in range(pos+1,len(self.__lista)): 
              if self.__lista[pos]["nombre"] > self.__lista[sig]["nombre"]:
                  aux = self.__lista[pos]
                  self.__lista[pos]=self.__lista[sig]
                  self.__lista[sig]=aux
      else:
          for pos in range(0,len(self.__lista)): 
           for sig in range(pos+1,len(self.__lista)): 
              if self.__lista[pos]["nombre"] < self.__lista[sig]["nombre"]:
                  aux = self.__lista[pos]
                  self.__lista[pos]=self.__lista[sig]
                  self.__lista[sig]=aux
          
        
notas = [
  {"nombre":"Ana","n1":60,"n2":40},
  {"nombre":"Daniel","n1":20,"n2":40}, 
  {"nombre":"Danny","n1":30,"n2":50},  
  {"nombre":"Dayana","n1":40,"n2":50}, 
  {"nombre":"Erick","n1":50,"n2":40},
  {"nombre":"Romina","n1":55,"n2":40},
 
   
] 
lista = [2,4,5,7,8,9,18,22,32,34,37]
bus1 = Busqueda(lista)
pos = bus1.buquedaBinaria(40)
print(pos)

    

   
    