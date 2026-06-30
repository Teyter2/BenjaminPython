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
    "A004":["24-03-2025","Pendinete"],
    "A005":["24-03-2024","24-07-2024"],
    "A006":["24-03-2024","24-09-2024"],
}

def autos_vendidos_por_marca(marca):
    total=0

    for id_auto, datos in autos.items():
        if datos[0].lower() == marca.lower():

            if operaciones[id_auto][1] != "Pendinte":
                total+=1

    print(total)

autos_vendidos_por_marca()