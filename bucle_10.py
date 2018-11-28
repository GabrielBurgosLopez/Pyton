def bucle_10():
    print "******************"
    print "* PARES O IMPARES*"
    print "******************"
    print "hasta que numero quieres conatar"
    nfinal= input("numero= ")
    #definimos una variable para contar los pares
    numero_pare=0 #inicializamos la variable a cero
    #Definimos otra variable para contar los impares
    numero_impares=0 #inicializamos la variable a cero
    for numero in range(1,nfinal+1):
        if(numero%2==0):
            print str(numero)," es par"
        else:
            print str(numero)," es impar"
            numero_pares=numero_pares+1
    print "he contado ",numero_pares, " numeros pares "
    print "he contado ",numero_impares " numeros impares "
bucle_10()
