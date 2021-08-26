#Ejercicio 1
"""
Created on Sun Jun 13 14:52:08 2021

@author: miguel
"""
"""

Ejercicio 1¶
Reescriba el programa del salario, para pagarle al empleado 1.5 veces la tarifa cuando se hayan trabajado horas extra (todas las horas que excedan de las 48 horas).

Ejemplo:

Ingrese Horas: 45
Ingrese tarifa: 1000

Paga: 45000.0

Ejemplo:

Ingrese Horas: 50
Ingrese tarifa: 1000

Paga: 51000.0
"""

horas_trabajadas = int(input("Ingrese Horas: "))
tarifa_hora = int(input("Ingrese tarifa: "))

if horas_trabajadas> 48 :
    horas_ext = horas_trabajadas - 48
    pago_tot = horas_ext *1.5*tarifa_hora + 48 *tarifa_hora
    
    print("Pago: ", pago_tot)

else: 
    pago_n = horas_trabajadas * tarifa_hora
    print("pago: ", pago_n)

    