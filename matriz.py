class Matriz:
    def __init__(self,matriz,nfilas,ncols):
        self.matriz  = matriz
        self.noFilas = nfilas
        self.noCols  = ncols
        
    def  ordenar(self):
        for fil in range(0,self.noFilas): 
           for col1 in range(0,self.noCols): 
             for col2 in range(col1+1,self.noCols): 
                if self.matriz[fil][col1] < self.matriz[fil][col2]:
                   aux = self.matriz[fil][col1]
                   self.matriz[fil][col1]=self.matriz[fil][col2]
                   self.matriz[fil][col2]=aux
                  
    
    def menor(self):
        menor   = -1
        for fila in range(self.noFilas):
            for col in range(self.noCols):
                if self.matriz[fila][col] > menor: 
                    mayor = self.matriz[fila][col]
        return mayor 
    
    def mayor(self):
        mayor   = 0
        for fila in range(self.noFilas):
            for col in range(self.noCols):
                if self.matriz[fila][col] > mayor: 
                    mayor = self.matriz[fila][col]
        return mayor 
    
    def ingresar(self):
          os.system("cls")
          self.matriz  = []
          for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)
      
    def mostrar(self):
      
        print("-----------------")  
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
        print("-----------------")                   
    def buscar(self,buscado):
        resp = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
               if self.matriz[fila][col] == buscado:
                   resp["fila"]=fila
                   resp["col"]=col
                   break
            if resp: break       
        return resp        
    
    def buscarW(self,buscado):
        resp = {}
        fila=0
        enc=False
        while fila < len(self.matriz) and enc==False:
            col=0
            while col < len(self.matriz[fila]) and enc==False:
               if self.matriz[fila][col] == buscado:
                   resp["fila"]=fila
                   resp["col"]=col
                   enc=True
               else: col +=1   
            fila +=1   
        return resp
    
    def sumar(self,mat2):
        matrizSuma  = []
        for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = self.matriz[fila][col] + mat2[fila][col] 
                columnas.append(valor)
            matrizSuma.append(columnas)
        return matrizSuma  
    
   
    def exponentes(self,exponente):
        matrizExponentes  = []
        for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = self.matriz[fila][col]
                resp = 1
                for exp in range(exponente):
                    resp = resp*valor
                columnas.append(resp)
            matrizExponentes.append(columnas)
        return matrizExponentes
      
numeros = [
    [1,3,5,7],
    [2,4,6,8],
    [3,6,9,12],
    [4,8,12,16]
]
mat1 = Matriz(numeros,4,4)
print(mat1.exponentes(2))
