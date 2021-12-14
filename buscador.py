class Buscador:
    def __init__(self,dato):
        self.lista=dato
    
    def  recorrerElemento(self):
        for ele in self.lista:
            print(ele,end=" ")
        
        for ele in self.lista[::-1]:
            print(ele,end=" ")
        
        print()
        for pos,ele in enumerate(self.lista):
            print("[{}]={}  ".format(pos,ele))
        print()
  
        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]={}  ".format(pos,self.lista[pos]))
    
    def buscar(self,buscado):
        encontrado=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                encontrado=True
                break
        
        if encontrado: return pos
        else: return -1          
    
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)-1): 
           for sig in range(pos+1,len(self.lista)): 
               if self.lista[pos] > self.lista[sig]:
                   aux = self.lista[pos]
                   self.lista[pos]=self.lista[sig]
                   self.lista[sig]=aux
    
    def ordenarDes(self):
        for pos in range(0,len(self.lista)-1): 
           for sig in range(pos+1,len(self.lista)): 
               if self.lista[pos] < self.lista[sig]:
                   aux = self.lista[pos]
                   self.lista[pos]=self.lista[sig]
                   self.lista[sig]=aux
     
    def primer(self):
        return self.lista[0] 
    
    def primerElemento(self):
       primero=self.lista[0]
       self.lista = self.lista[1:]   
       return primero      
   
    def primerElemento2(self):
       primero=self.lista[0]
       auxlista=[]
       for pos in range(1,len(self.lista)):
           auxlista.append(self.lista[pos])
       self.lista=auxlista       
       return primero      
    
    def ultimo(self):
        return self.lista[-1] 
    
    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        self.lista = self.lista[:-1]   
        return ultimo  
   
    def ultimoEliminado2(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista       
        return ultimo  
    
    def insertar(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
        self.lista= self.lista[0:pos] + auxlista + self.lista[pos:]
        
    def insertar2(self,num):
        self.lista.append(num)
        self.ordenarAsc()     
# pos
    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break
        if enc: self.lista= self.lista[0:pos]  + self.lista[pos+1:]
   
    def eliminar2(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break
        if enc:
            auxlista=[]
            for i in range(0,pos):
                auxlista.append(self.lista[i])
                
            for j in range(pos+1,len(self.lista)):
                auxlista.append(self.lista[j])
                
            self.lista=auxlista        
    

datos = [40,35,20,30,50] 
 #        0  1  2  3  4 5
num=20
# datos.sort()
#print(datos)
bus = Buscador(datos)
print(bus.lista)
bus.eliminar2(num)
print(bus.lista)
# bus.ordenarAsc()
# print(bus.lista)
# bus.ordenarDes()
# print(bus.lista)

#buscado=9
#        0 1 2 3 4
#datos="Hola"

#bus.recorrerElemento()
# valor=9
# resp= bus.buscar(valor)
# if resp !=-1: print("el numero:{} se encuentra en la posiocion:[{}] de la lista:{}".format(valor,resp,bus.lista))
# else: print("el numero:{} no se encuentra en la  lista:{}".format(valor,bus.lista))
# numerosBuscados = (2,4,6,1)
# respuestas = {}
# for valor in numerosBuscados:
#     resp= bus.buscar(valor)
#     if resp !=-1: respuestas[valor]=resp
# print(respuestas)