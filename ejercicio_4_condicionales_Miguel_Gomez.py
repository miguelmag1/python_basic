# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:14:06 2021

@author: miguel
"""


  
print("""
  ________                     __    .__                                                
 /  _____/   __ __    ______ _/  |_  |__|   ____   _____      _____   ______     ____   
/   \  ___  |  |  \  /  ___/ \   __\ |  | _/ ___\  \__  \    /     \  \____ \   /  _ \  
\    \_\  \ |  |  /  \___ \   |  |   |  | \  \___   / __ \_ |  Y Y  \ |  |_> > (  <_> ) 
 \______  / |____/  /____  >  |__|   |__|  \___  > (____  / |__|_|  / |   __/   \____/  
        \/               \/                    \/       \/        \/  |__|                                                                           
                    Las delicias del campo a la puerta de tu casa     

Bienvenido a gusticaja el software de facturacion para productos al por mayor de gusticampo
                         """)


try:
    opcion = int(input("seleccione una de las siguientes opciones: (1) para crear una factura\n(2)para generar un reporte" ))

    if opcion ==1:
        tempf = float(input("Inserte temperatura (°F): "))
        tempc= (tempf-32)*(5/9)
        tempc_red = round(tempc,2)
        print("Temp en °C:",tempc_red)  
        #pasando de f a c
    elif opcion>= 2 and opcion<3:
        tempc = float(input("Inserte temperatura (°C): "))
        #(0 °C × 9/5) + 32
        tempf= (tempc*(9/5)+32)
        tempc_red = round(tempf,2)
        print("Temp en °C:",tempc_red) 
    else:
        print("Inserte la opción 1 o 2")
except:
    print("Error, por favor ingrese un número")