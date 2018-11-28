def cambio():
    respuesta=input("introduce una cantidad de euros: ")
    respuesta=raw_input("dolares o libras (d/1)?: ")
    if(respuesta== "d"):
        moneda_nueva=euros*1.15
        unidades="dolares"
    else:
        moneda_nueva=euros*0.88
        unidades="libras"
    print "son "+ moneda_nueva +" "+ unidades

cambio()
    
