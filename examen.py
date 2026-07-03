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

def muestrAutos(d):
    for id, vehiculo in d.items():
        print(f"{ id }: {vehiculo}")
    print("="*30)

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
                
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1] = nueva_fecha
        return True
    else:
        return False
    
def validaString(h):
    if h=="" or h==" ":
        return True
    else:
        return False 
def validaAño(a):
    if a <1900:
        return True
    else:
        return False
def validaRanking(a):
    if a>=1 and a<=5:
        return False
    else:
        return True
    
print(validaRanking(5))

def creAuto():
    id=input("Ingresa el nuevo ID: ")
    if validaString(id):
        print("Dato inválido")
        return
    marca=input("Ingresa la marca: ")
    if validaString(marca):
        print("Dato inválido")
        return
    modelo=input("Ingresa el nuevo modelo: ")
    if validaString(modelo):
        print("Dato inválido")
        return
    año=int(input("Ingresa el año: "))
    if validaAño(año):
        print("El año debe ser superior a 1900")
        return
    ranking=int(input("Ingresa el ranking: "))
    if validaRanking(ranking):
        print("El ranking debe estar entre 1 y 5")
        return
    fecha=input("Ingrese la fecha ( dd-mm-yyyy): ")
    if validaString(fecha):
        print("Dato inválido")
        return
    autos[id]=[marca, modelo,año,ranking]
    operaciones[id]=[fecha,'Pendiente']

def  eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False

def menu():
   while True:
      try:
         print("="*20)
         print("1.- ")
         print("2.- ")
         print("3.- ")
         print("4.- ")
         print("5.- ")
         print("6.- ")
         print("7.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                 muestrAutos()
               case 2:
                 autos_vendidos_por_marca()
               case 3:
                 busqueda_por_año()
               case 4:
                 actualizar_fecha_venta()
               case 5:
                 eliminar_auto()
               case 6:
                 creAuto()
               case 7:
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)

#=test=

# while True:
#     id=input("Ingrese el id del auto: ")
#     fecha=input("Ingrese la fecha de venta: ")

#     if actualizar_fecha_venta(id,fecha):    
#         print("Exito, nueva fecha de venta actualizada")
#     else:
#         print("Metió mal las manos")
#     next=input("Desea actualizar otro vehículo (s/n)?")
#     if next.lower()=="n":
#         break 

# while True:
#     try:
#         año_inicio = int(input("Ingrese el año de inicio de la : "))
#         año_termino = int(input("Ingrese el año de termino de la busqueda: "))
#         busqueda_por_año(año_inicio, año_termino)
#         break
#     except:
#         print("los años deben ser números enteros")

# print(validaString(" "))

# muestrAutos(autos)
# creAuto()
# muestrAutos(autos)

# busqueda_por_año(2010,2026)
# autos_vendidos_por_marca("Ford")
# print(marca, modelo ,".-", año,"--",id_auto)