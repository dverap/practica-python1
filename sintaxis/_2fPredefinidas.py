# funciones matematicas
import math
print("funciones matematicas")
num1, num2,num,men = 12.572,15.4,4,'1234'
print("num1=",num1," ceil=",math.ceil(num1)," floor=", math.floor(num1)," trunc=",math.trunc(num1),
" round=",round(num1,2),round(num1,1),round(num1,0))
print(math.pow(num,3),math.sqrt(num),math.cos(num))
print("num=",num,type(num),"num1=",num1,type(num1),"men=",men,type(men))
print("num=",num,float(num),"num1=",num1,int(num1),"men=",men,int(men),"num2=",num2,str(num2))
# funciones de cadenas
print("funciones de cadenas")
mensaje = 'Hola ' + 'mundo ' + 'Python'
print(mensaje)
print(mensaje[0:4],mensaje[::-1],mensaje[:])
print(mensaje[0],mensaje[5:len(mensaje)],mensaje[-1])
print(mensaje.find("mundo"))
print("minuscula={}, mayuscula={}".format(mensaje.lower(),mensaje.upper()))
print('Hola\tHola\tHola\nMundo')
men1= mensaje.split()
men2 =' '.join(men1)
print(men1, men2,len(mensaje))
mensaje=mensaje.replace(" ",";")
print(mensaje)
men1= mensaje.split(";")
men2 =';'.join(men1)
print(men1, men2)
print("*"*5,"_"*5)
# funciones de fechas
from datetime import datetime,timedelta,date
today = date.today()#Día actual
now = datetime.now() 
print("today={} now={}".format(today,now))
#Date
print(today)
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)
print(new_date)
# operaciones
#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
#Comparación
if now < new_date:
    print("La fecha actual={} es menor que la nueva fecha={}".format(now,new_date))
  
#formato de fechas
format1 = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
format2 = now.strftime('%Y-%M-%d') # fecha en string
fecha_dt = datetime.strptime(format2,'%Y-%M-%d') # convierte fecha string a fecha
print(format1,type(format1))
print(type(fecha_dt),fecha_dt + timedelta(days=2))
# fecha Formateada
months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
day = today.day
month = months[today.month - 1]
year = today.year
fecha = "{} de {} del {}".format(day, month, year)
print(fecha)
fecha_birth = datetime.strptime('1969-05-21','%Y-%M-%d')
difdias = now - fecha_birth
print(difdias)
dif= ((now.month, now.day) < (fecha_birth.month, fecha_birth.day)) 
edad = now.year - fecha_birth.year + dif
print("fecha Nacimento={} fecha Actual={} edad={}".format(fecha_birth,now,edad))