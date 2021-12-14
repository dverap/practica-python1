class Ejemplo1:
    def __init__(self):
        pass
    
    def pagoTotal(self):
        tc = int(input("Ingrese total compra"))
        des = tc*0.15
        pago = tc -des
        print("Tcompra:{} Des:{} Valor Pagar:{}".format(tc,des,pago))
        
eje1 = Ejemplo1()
eje1.pagoTotal()

