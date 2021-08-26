# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:07:57 2021

@author: miguel
"""
#cuanto vale ir a la oficina 
try:
    g_quincena = int(input("Ingrese lo que ganó esta quincena: "))

    Dias_oficina = int(input("Ingrese el número de días que va a la oficina: "))
    tipo_transporte = int(input("tomó taxi alguna vez? 1 para si 2 para no "))
    if tipo_transporte >=1 and tipo_transporte<2:
        try:
            veces_taxi=int(input("cuantaas veces tomó taxi entre ida y vualta a la oficina en la quincena "))
            try:    
                val_taxi = int(input("cuanto le vale el taxi en promedio: "))
                tot_taxi_15na = val_taxi* veces_taxi
                try:
                    val_bus = int(input("cuanto vale el pasaje de bus a la oficina "))
                    tot_transporte = (Dias_oficina*2-veces_taxi)*val_bus
                    try:
                            comida_fuera =int(input("compró alguna vez su almuerzo al ir a la oficina? 1 para si 2 para no "))
                    except:
                        print("inserte un numero ")
                except:
                    print("inserte un numero ")
            except:
                print("inserte un numero ")
        except:
            print("inserte un numero ")
        
        if comida_fuera >=1 and comida_fuera <2:#si compro
         try:  
            veces_compro_almuerzo=int(input("cuantaas veces compró su almuerzo en la oficina: "))
            try:
                precio_almuerzo = int(input("cuanto le vale el almuerzo en la ogicina? "))
                tot_val_almuerzo_comp = veces_compro_almuerzo*precio_almuerzo
                tot_ir_oficina = tot_transporte + tot_val_almuerzo_comp
                dinero_sobra = g_quincena - tot_ir_oficina
                print("usted gastó ", tot_transporte, " en transporte durante la quincena ")
                print("usted gastó ", tot_val_almuerzo_comp,"en almuerzos durante la quincena ")
                print("usted gastó ", tot_ir_oficina, "yendo a la oficina ")
                print("le quedan ", dinero_sobra," despues de ir a la oficina ")
            except:
                print("Inserte un numero")
         except:
            print("Inserte un numero")
            
        elif  comida_fuera >=2 and comida_fuera <3: #NO compro:
            tot_ir_oficina = tot_transporte 
            dinero_sobra = g_quincena - tot_ir_oficina
            print("usted gastó ", tot_transporte, " en transporte durante la quincena ")
            print("no gastó en almuerzos ")
            print("usted gastó ", tot_ir_oficina, "yendo a la oficina ")
            print("le quedan ", dinero_sobra," despues de ir a la oficina ")
        else:
            print("introduzca un numero valido ")
    elif tipo_transporte >= 2 and tipo_transporte<3:
        try:
            val_bus = int(input("cuanto vale el pasaje de bus a la oficina "))
            tot_transporte = (Dias_oficina*2)*val_bus
            try:
                comida_fuera =int(input("compró alguna vez su almuerzo al ir a la oficina? 1 para si 2 para no "))
            except:
                print("Inserte un numero")
        except:
            print("Inserte un numero")
        if comida_fuera >=1 and comida_fuera <2:#si compro
            try:
                veces_compro_almuerzo=int(input("cuantaas veces compró su almuerzo en la oficina: "))
                try:
                    precio_almuerzo = int(input("cuanto le vale el almuerzo en la ogicina? "))
                    tot_val_almuerzo_comp = veces_compro_almuerzo*precio_almuerzo
                    tot_ir_oficina = tot_transporte + tot_val_almuerzo_comp
                    dinero_sobra = g_quincena - tot_ir_oficina
                    print("usted gastó ", tot_transporte, "en transporte durante la quincena")
                    print("usted gastó ", tot_val_almuerzo_comp,"en almuerzos durante la quincena ")
                    print("usted gastó ", tot_ir_oficina, "yendo a la oficina ")
                    print("le quedan ", dinero_sobra," despues de ir a la oficina ")
                except:
                    print("Inserte un numero")
            except:
                print("Inserte un numero")
        elif  comida_fuera >=2 and comida_fuera <3: #NO compro:
            tot_ir_oficina = tot_transporte 
            dinero_sobra = g_quincena - tot_ir_oficina
            print("usted gastó ", tot_transporte, "durante la quincena ")
            print("no gastó en almuerzos ")
            print("usted gastó ", tot_ir_oficina, "yendo a la oficina ")
            print("le quedan ", dinero_sobra," despues de ir a la oficina ")
        
        else:
            print("introduzca un numero valido ")
    else:
        print("inserte una opcion valida de transporte 1 o 2 ")
except:
    print("incerte un numero ")


    
