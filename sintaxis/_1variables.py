class Sintaxis:
    # __init__ Metodo constructor se ejecuta cuando se instancia la clase cuyo objetivo es crear 
    # e inicializar  los atributos de la clase. Self es un objeto que representa la clase creada 
    def __init__(self,dato="instancia de la clase"):
        self.frase=dato
    
    def usoVariables(self):
        edad, __peso = 50, 70.5
        nombres = "Daniel Vera"
        #          012345678910
        Tipo_sexo = 'M'
        civil = True
        # print("civil={} y su tipo es:{}".format(civil,type(civil)))
         # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario = ('dchiki', 1234, 'chiki@gmail.com',True)
        #              0       1           2          3
        #usuario[4]="milagro"
        x = usuario[0]
        # listas = [] Son colecciones mutables
        materias = ['Programacion Web', 'Php', 'POO']
        #                 0               1      2
        materias[1]="Python"
        materias.append("Go")
        # diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        docente["edad"]=51
        docente["cargo"]="Docente"
        y=docente["cargo"]
        #print(nombres,nombres[0],nombres[0:2],nombres[-1])
        #print(usuario,usuario[0],usuario[0:2],usuario[-1])
        #print(materias,materias[2:],materias[:2],materias[:-1],materias[-2:] )
        print(x,y)
        print(docente,docente['nombre'])
  
    def mostrar(self):
        print("mostrar")
        print(self.frase)
        
ejer1 = Sintaxis() #instancia la clase(ejecuta __init__) y se crea el objeto1 con todos los atributos y metodos de la clase sintaxis     
ejer1.usoVariables() 
