# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:20:38 2021

@author: miguel
"""
"""
Ejercicio 5

Modifique el programa del vendedor en un caso en el que un 
bien por encima de 500 mil pesos tenga un IVA de 25% y por 
debajo de 50 mil esté exento de IVA.

Bonus: Haga que el programa reciba 2 bienes diferentes 
y entregue el consolidado. Bonus 2: Haga que el programa 
lidie con errores de ingreso del usuario.

"""


"""
valorTotal = float(input("Inserte valor tota : "))

valorIva = valorTotal*0.19
valorBien= -valorIva+valorTotal

print("Valor del bien: ", int(valorBien))
print("Impuesto:", int(valorIva))


"""
try:
    bien_1= int(input("Introduzca el valor del primer bien antes del IVA: "))
    try:
        bien_2= int(input("Introduzca el valor del segundo bien antes del IVA: "))

        if bien_1>500000:
            valor_neto_bien1= (bien_1 *0.25)+bien_1
            # bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
            if bien_2>500000:
                valor_neto_bien2= (bien_2 *0.25)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                pago_iva_b1= bien_1*0.25
                pago_iva_b2= bien_2*0.25
                
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
                
            elif bien_2 <=500000 and bien_2 >= 50000:
                valor_neto_bien2= (bien_2 *0.19)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                pago_iva_b1= bien_1*0.25
                pago_iva_b2= bien_2*0.19             
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
                
            elif bien_2<50000:
                valor_neto_bien2= bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
              
                pago_iva_b1= bien_1*0.25
                pago_iva_b2= bien_2*0                
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
            else:
                print("valor no valido")
            
        elif bien_1<=500000 and bien_1>=50000:
            valor_neto_bien1= (bien_1 *0.19)+bien_1
            #bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
            if bien_2>500000:
                valor_neto_bien2= (bien_2 *0.25)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                
                pago_iva_b1= bien_1*0.19
                pago_iva_b2= bien_2*0.25                
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 1: ", valor_neto_bien2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total a pagar: ", Valor_a_pagar)
            elif bien_2 <=500000 and bien_2 >= 50000:
                valor_neto_bien2= (bien_2 *0.19)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                
                pago_iva_b1= bien_1*0.19
                pago_iva_b2= bien_2*0.19                
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
            elif bien_2<50000:
                 valor_neto_bien2= bien_2
                 Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                 
                 pago_iva_b1= bien_1*0.25
                 pago_iva_b2= bien_2*0                
                 print("valor a pagar IVA producto 1: ", pago_iva_b1)
                 print("valor a pagar IVA producto 2: ", pago_iva_b2)
                 print("valor a pagar Bien 1 sin IVA: ", bien_1)
                 print("valor a pagar Bien 2 sin IVA: ", bien_2)
                 print("valor total bien 1: ", valor_neto_bien1)
                 print("valor total bien 2: ", valor_neto_bien2)
                 print("valor total a pagar: ", Valor_a_pagar)
            else:
                print("valor no valido")
        elif bien_1<50000:
            valor_neto_bien1= bien_1 
            # bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
            if bien_2>500000:
                valor_neto_bien2= (bien_2 *0.25)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                
                pago_iva_b1= bien_1*0
                pago_iva_b2= bien_2*0.25                
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
            elif bien_2 <=500000 and bien_2 >= 50000:
                valor_neto_bien2= (bien_2 *0.19)+bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                
                pago_iva_b1= bien_1*0
                pago_iva_b2= bien_2*0.19               
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
                
            elif bien_2<50000:
                valor_neto_bien2= bien_2
                Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
                
                pago_iva_b1= bien_1*0
                pago_iva_b2= bien_2*0               
                print("valor a pagar IVA producto 1: ", pago_iva_b1)
                print("valor a pagar IVA producto 2: ", pago_iva_b2)
                print("valor a pagar Bien 1 sin IVA: ", bien_1)
                print("valor a pagar Bien 2 sin IVA: ", bien_2)
                print("valor total bien 1: ", valor_neto_bien1)
                print("valor total bien 2: ", valor_neto_bien2)
                print("valor total a pagar: ", Valor_a_pagar)
                
            else:
                print("valor no valido")
        else:
            print("no se vale")
    except:
        print("Error, por favor ingrese un número")
except:
    print("Error, por favor ingrese un número")