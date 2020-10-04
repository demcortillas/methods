def GEOCODIGO(comuna,distrito,area,zona):
    c=str(comuna)
    d=str(distrito)
    a=str(area)
    z=str(zona)

    #Distrito
    if distrito > 9:
        d2=d
    else: d2=str("0")+d
    #Zona
    if zona > 9 and zona < 100:
        z2=str("0")+z
    elif zona > 99 and zona < 1000:
        z2=z
    elif zona < 10:
        z2=str("00")+z
    #Codigo
    codigo=c+d2+a+z2
    return codigo