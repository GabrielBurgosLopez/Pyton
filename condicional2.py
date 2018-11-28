def condicional_2():
    respuesta=input("cual es tu edad? ")
    if(edad >= 18 ):
        print "sala alcoholica"
    else:
        if(edad >= 15 ):
            print "sala adolescentes"
        else:
            print "sala infantil"

condicional_2()
