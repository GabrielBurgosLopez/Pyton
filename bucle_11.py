def bucle_11():
    print "******************"
    print "* PARES O IMPARES*"
    print "******************"
    print "hasta que numero quieres conatar"
    nfinal= input("numero= ")
    #definimos una variable para sumar los pares
    suma_pares=0 #inicializamos la variable a cero
    #Definimos otra variable para sumar los impares
    suma_impares=0 #inicializamos la variable a cero
    for numero in range(1,nfinal+1):
        if(numero%2==0):
            print str(numero)," es par"
            suma_pares=suma=suma_pares+numero
        else:
            print str(numero)," es impar"
            suma_impares=numero_pares+1
    print "he contado ",numero_pares, " numeros pares "
    print "he contado ",numero_impares " numeros impares "
bucle_11()
