class Calculadora:
    def __init__(self,n1,n2):
        valor = n1+n2
        self.num1= valor
        self.__num2= n2              
    
    def suma(self,n1):
      pass
     
    def resta(self,n2):
       pass
    def mostrar(self,x):
        pass
        

# num1 y __num2 tienen ambito global para toda la clase
# n1 , n2 y valor del metodo constructor tiene ambito local 
# n1 de suma, n2 de resta y x del metodo mostrar() solo pueden ser usadas en sus propios metodos() 
# cuando se instancia la clase Calculadora de los atributos del constructor solo num1 pueder ser referenciada en el objeto creado

# num1 y __num2 tienen ambito global para toda la clase y para cualquier objeto que la instancie
# n1 , n2 y valor del constructor tiene ambito local es decir no pueden ser usadas en los metodos suma y resta
# n1 de suma, n2 de resta y x de mostrar solo pueden ser usadas en sus propios metodos
# cuando se instancia la clase solo num1 pueder ser referenciada

# num1 y __num2 tienen ambito global para toda la clase y cualquier objeto que la instancie
# n1 , n2 y valor del constructor tiene ambito local es decir pueden ser usadas en los objetos instanciados
# n1 de suma, n2 de resta y x de mostrar solo pueden ser usadas en sus propios metodos
# cuando se instancia la clase solo num1 pueder ser referenciada

# num1 y __num2 tienen ambito global para toda la clase 
# n1 , n2 y valor del constructor tiene ambito local
# n1 de suma, n2 de resta y x de mostrar solo pueden ser usadas en sus propios metodos
# cuando se instancia la clase tanto num1 y __num2 pueden ser referenciadas


# class Pila:
#     def __init__(self,tamanio):
#         self.__lista = [] 
#         self.__tope =0
#         self.size=tamanio

#     def empty(self):
#         return self.__tope == 0
    
#     def push(self,dato):
#         if self.__tope < self.size:
#             self.__lista = self.__lista + [dato]
#             self.__tope += 1
#         else:
#             print("La lista esta LLena")
                
#     def pop(self):
#         if self.empty():
#             return None
#         else:
#             top = self.__lista[-1]
#             self.__tope -= 1
#             self.__lista = self.__lista[:-1]
#             return top
    
#     def show(self):
#             print("{}".format(self.__lista[self.__tope-1]))
        
#     def longitud(self):
#         return self.__tope   
    
# pila = Pila(10)  
# pila.push(4)    
# pila.push(6)    
# x=pila.pop()
# y=pila.pop()
# pila.push(7)
# pila.push(y)
# pila.push(x)
# pila.pop()
# pila.show()


class Matriz:
    def __init__(self,matriz,nfilas,ncols):
        self.matriz  = matriz
        self.noFilas = nfilas
        self.noCols  = ncols
        
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

#     def  ordenar(self):
#         for fil in range(0,self.noFilas): 
#            for col1 in range(0,self.noCols): 
#              for col2 in range(col1+1,self.noCols): 
#                 if self.matriz[fil][col1] < self.matriz[fil][col2]:
#                    aux = self.matriz[fil][col1]
#                    self.matriz[fil][col1]=self.matriz[fil][col2]
#                    self.matriz[fil][col2]=aux
                  
    
#     def menor(self):
#         menor   = -1
#         for fila in range(self.noFilas):
#             for col in range(self.noCols):
#                 if self.matriz[fila][col] > menor: 
#                     mayor = self.matriz[fila][col]
#         return mayor 
    
#     def mayor(self):
#         mayor   = 0
#         for fila in range(self.noFilas):
#             for col in range(self.noCols):
#                 if self.matriz[fila][col] > mayor: 
#                     mayor = self.matriz[fila][col]
#         return mayor 
    
#     def ingresar(self):
#           os.system("cls")
#           self.matriz  = []
#           for fila in range(self.noFilas):
#             columnas = []
#             for col in range(self.noCols):
#                 valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
#                 columnas.append(valor)
#             self.matriz.append(columnas)
      
#     def mostrar(self):
      
#         print("-----------------")  
#         for fila in range(len(self.matriz)):
#             #print(self.matriz[fila])
#             for col in range(len(self.matriz[fila])):
#                 print("[{}]".format(self.matriz[fila][col]),end=" ")
#             print()
#         print("-----------------")                   
#     def buscar(self,buscado):
#         resp = {}
#         for fila in range(len(self.matriz)):
#             for col in range(len(self.matriz[fila])):
#                if self.matriz[fila][col] == buscado:
#                    resp["fila"]=fila
#                    resp["col"]=col
#                    break
#             if resp: break       
#         return resp        
    
#     def buscarW(self,buscado):
#         resp = {}
#         fila=0
#         enc=False
#         while fila < len(self.matriz) and enc==False:
#             col=0
#             while col < len(self.matriz[fila]) and enc==False:
#                if self.matriz[fila][col] == buscado:
#                    resp["fila"]=fila
#                    resp["col"]=col
#                    enc=True
#                else: col +=1   
#             fila +=1   
#         return resp
    
#     def sumar(self,mat2):
#         matrizSuma  = []
#         for fila in range(self.noFilas):
#             columnas = []
#             for col in range(self.noCols):
#                 valor = self.matriz[fila][col] + mat2[fila][col] 
#                 columnas.append(valor)
#             matrizSuma.append(columnas)
#         return matrizSuma  
    
   
      
numeros = [
    [1,3,5,7],
    [2,4,6,8],
    [3,6,9,12],
    [4,8,12,16]
]
mat1 = Matriz(numeros,4,4)
print(mat1.exponentes(2))
