def bucle_7():
    print "*******************************"
    print "* EL CONSTRUCTOR DE PIRAMIDES *"
    print "*******************************"
    print "Indica, oh faraon, de que altura deseas tu piramide: "
    altura=input("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,altura+1):
            print "*"

bucle_7()
