bien_1= int(input(print("Introduzca el valor del primer bien: ")))

if bien_1>500:
    valor_neto_bien1= (bien_1 *0.25)+bien_1
    bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
    if bien_2>500:
        valor_neto_bien2= (bien_2 *0.25)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2 <=500 and bien_2 >= 50:
        valor_neto_bien2= (bien_2 *0.19)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2<50:
        valor_neto_bien2= bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    else:
        print("valor no valido")
            
elif bien_1<=500 and bien_1>=50:
    valor_neto_bien1= (bien_1 *0.19)+bien_1
    bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
    if bien_2>500:
        valor_neto_bien2= (bien_2 *0.25)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2 <=500 and bien_2 >= 50:
        valor_neto_bien2= (bien_2 *0.19)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2<50:
        valor_neto_bien2= bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    else:
        print("valor no valido")
elif bien_1<50:
    valor_neto_bien1= bien_1 
    bien_2= int(input(print("Introduzca el valor del segundo bien: ")))
    if bien_2>500:
        valor_neto_bien2= (bien_2 *0.25)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2 <=500 and bien_2 >= 50:
        valor_neto_bien2= (bien_2 *0.19)+bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    elif bien_2<50:
        valor_neto_bien2= bien_2
        Valor_a_pagar = valor_neto_bien2 +valor_neto_bien1
        print("valor total a pagar: ", Valor_a_pagar)
    else:
        print("valor no valido")
else:
    print("no se vale")