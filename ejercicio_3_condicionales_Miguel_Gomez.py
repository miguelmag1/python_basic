#Ejercicio_3
"""
Created on Sun Jun 13 17:15:45 2021

@author: miguel
"""
"""
Ejercicio 3
Reescriba el programa de la Casa de cambio
para que el precio esté fijado y se requiera 
solo saber hace cuántos días el usuario hizo 
la compra
(Tip: Use la TRM)   
"""
# pedir el dia 
pesos = input("Inserte cantidad comprada en pesos: ")
pesos = int(pesos)
dia_transaccion =input("Hace cuántos días hizo la compra: ")
dia_transaccion= int(dia_transaccion)

# seccion de condicional trm, dentro de cada condicional hacer las funcones 
if dia_transaccion >= 0 and dia_transaccion <1:#  ayer 
    trm = 3626
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM de hoy es", trm)

elif dia_transaccion > 0 and dia_transaccion <=1:#  ayer 
    trm = 3500
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)

elif dia_transaccion > 1 and dia_transaccion <=2:# hace 2 dias 
    trm = 3500
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 2 and dia_transaccion <=3 : #hace 3 dias 
    trm = 3550
    dolares = pesos//trm
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 3 and dia_transaccion <= 4: #hace 4 dias 
    trm = 3400
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 4 and dia_transaccion <= 5: #hace 5 dias 
    trm = 3450
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 5 and dia_transaccion <= 6: #hace 6 dias 
    trm = 3700
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 6 and dia_transaccion <= 7:#hace 7 dias 
    trm = 3800
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    
elif dia_transaccion > 7 and dia_transaccion <= 8: #hace 8 dias 
    trm = 3900
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
else:
    trm = 3626
    dolares = pesos//trm 
    cambio = pesos%trm
    print("Compró: USD", dolares)
    print("Le sobran:", cambio,"COP")
    print("el TRM del dia fue", trm)
    