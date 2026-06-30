autos = {
    "A001":["Toyota","corolla",2010,5],
    "A002":["Ford","Ranger",2019,4],
    "A003":["Chevrolet","Spark",2022,4],
    "A004":["Suzuki","Aerio",2000,4],
    "A005":["Toyota","Yaris",2015,5],
    "A006":["Toyota","Impala",1950,1],
}


operaciones = {
    "A001":["01-01-2024","12-12-2015"],
    "A002":["07-08-2024","01-08-2025"],
    "A003":["09-01-2025","Pendiente"],
    "A004":["24-03-2025","Pendiente"],
    "A005":["24-03-2024","24-07-2024"],
    "A006":["24-03-2024","24-09-2024"],
}

def autos_vendidos_por_marca(marca):
    total=0

    for id_auto, datos in autos.items():
        if datos[0].lower() == marca.lower():

            if operaciones[id_auto][1] != "Pendinte":
                total+=1

    print("el numero todal de auntos vendidos de",marca.upper(),"es",total)

def busqueda_por_año(año_min, año_max):
    elementos=[]

    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        año = datos[2]

        if año_min <= año <= año_max:
            if operaciones[id_auto][1] == "Pendiente":

                elementos.append(f"{marca} {modelo} -- {id_auto}")

    if elementos.sort():
        print(elementos)
    else:
        print("No se ha encontados elementos :C ")
                
        


#test
while True:
    try:
        año_inicio = int(input("Ingrese el año de inicio de la : "))
        año_termino = int(input("Ingrese el año de termino de la busqueda: "))
        busqueda_por_año(año_inicio, año_termino)
        break
    except:
        print("los años deben ser números enteros")
    
busqueda_por_año(2010,2026)
# autos_vendidos_por_marca("Ford")
# print(marca, modelo ,".-", año,"--",id_auto)