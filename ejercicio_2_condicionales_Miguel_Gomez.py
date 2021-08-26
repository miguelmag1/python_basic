#Ejercicio_2
"""
Created on Sun Jun 13 16:23:03 2021

@author: miguel


Ejercicio 2
Reescriba el programa del salario, esta vez usando try y except para manejar inputs no numéricos con elegancia.

Ejemplo:

Ingrese horas: 20
Tarifa: quinientos mil
Error, por favor ingrese un número

Ingrese horas: veinte
Error, por favor ingrese un número

"""
try:
    horas_trabajadas = int(input("Ingrese Horas: "))
    try:
        tarifa_hora = int(input("Ingrese tarifa: "))
        if horas_trabajadas> 48 :
            horas_ext = horas_trabajadas - 48
            pago_tot = horas_ext *1.5*tarifa_hora + 48 *tarifa_hora
            print("Pago: ", pago_tot)

        else: 
            pago_n = horas_trabajadas * tarifa_hora
            print("pago: ", pago_n)

    except:
        print("Error, por favor ingrese un número")
except:
    print("Error, por favor ingrese un número")



    