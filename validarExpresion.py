from pilaEstatica import PilaEstatica

class ValidaExpresion:
    def __init__(self,expresion):
        self.expresion = expresion

    def validaParentesis(self):
        pila = PilaEstatica(len(self.expresion))
        for car in self.expresion:
            if car in("("):
                pila.push(car)
            else:
                if car == ')' and pila.pop() != "(":
                        break
              
        if pila.empty(): return True        
        else: return False            
                                
expresion = input("Ingrese Expresion: ")    
valida = ValidaExpresion(list(expresion))
print(valida.validaParentesis())