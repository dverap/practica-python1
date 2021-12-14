class Tarea:
    def __init__(self):
        pass
    def calculoPago(self):
        ht, he, het=0,0,0
        ph,  phe, pt =0,0,0
        ht = int(input("Ingrese horas trabajadas: "))
        ph = float(input("Ingrese valor hora: "))
        if ht > 40:
           print("En proceso de calculo...")
           he = ht -40
           if he > 8:
               het = he - 8
               he=8
               phe = ph * 2 * he + ph * 3 * het
           else:
              phe = ph * 2 * he 
           pt = ph*40 +  phe   
        else:
           pt = ph * ht
        
        print("El pago total de horas trabajadas es:", pt)
           
    def factorial(self):
        n = int(input("Ingrese cantidad de numeros: "))
        for i in range(n): 
            numero = int(input("Ingrese numero: "))
            # calculo del factorial
            fact=1 
            # while num > 0:
            #      fact=fact*num
            #      num = num -1
            for num in range(numero,0,-1): 
                  fact=fact*num
           
            print("factorial del numero:{} es:{}".format(numero,fact))
            
        
       
tarea = Tarea()
tarea.factorial()

        
        
    