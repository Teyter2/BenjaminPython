# def mostrar():
#     for d,p in pacientes.items():
#         print(d,p)
#     print("="*20)
# def agregar():
#     nombre=input("Que producto quiere agregar?: ")
#     precio=int(input("cual es el precio del producto?: "))
#     if pacientes:
#         datonuevo = max(pacientes.keys()) + 1
#     else:
#         datonuevo = 1
#     pacientes[datonuevo] = {"nombre": nombre, "precio": precio}
#     print("se agrego un nuevo producto")
#     print("="*20)
# def borrar():
#     try:
#         mostrar()
        # eliminar=int(input("que producto quiere borrar: "))
#         del pacientes[eliminar]
#         print("producto borrado")
#     except ValueError:
#         print("eliga una opcion numerica")
# def actualizar():
#     if not pacientes:
#         print("No hay productos para actualizar")
#         return
#     mostrar()
#     try:
#         actualizar = int(input("¿Qué producto quiere actualizar?: "))

#         if actualizar in pacientes:
#             print(f"Actualizando: {pacientes[actualizar]['nombre']}")
#             nuevonombre = input("Nuevo nombre (Enter para no cambiar): ")
#             if nuevonombre:
#                 pacientes[actualizar]["nombre"] = nuevonombre
#             nuevoprecio = input("Nuevo precio (Enter para no cambiar): ")
#             if nuevoprecio:
#                 pacientes[actualizar]["precio"] = int(nuevoprecio)
#             print("Producto actualizado")
#         else:
#             print("Ese producto no existe")
#     except ValueError:
#         print("Por favor, ingrese un número válido")

# pacientes=[
#     {"nombre": " Aquiles Baeza",  "prevision": "fonasa",
#      "temperatura": 34.6, "grave": True},
#     {"nombre": " Aquiles Baeza",  "prevision": "fonasa",
#     "temperatura": 34.6, "grave": True},
#     {"nombre": " Aquiles Baeza",  "prevision": "fonasa",
#     "temperatura": 34.6, "grave": True}
# ]
# while True:
#     print("""
# 1.Agregar 
# 2.Borrar 
# 3.Actualizar 
# 4.Mostrar 
# 5.Salir
# """)
#     print("="*20)
#     op=int(input("seleccione una opcion: "))
#     match op:
#         case 1:
#             agregar()
#         case 2:
#             borrar()
#         case 3:
#             actualizar()
#         case 4:
#             mostrar()
#         case 5:
#             print("Hasta pronto")
#             break  
#         case _:
#             print("ingrese unaa opcion valida del 1 al 5")
def mostrar():
    if len(pacientes)== 0:
        print("no hay pacientes")
    else:
        c=1
        for d in enumerate(pacientes, 1):
            print(f"{c}.-{d}")
            c+=1
        print("="*20)
def borrar():
    mostrar()
    eliminar=int(input("Que paciente quiere borrar?: "))
    pacientes.pop(eliminar-1)
    print("="*20)
def agregar():
    while True:
        try:
            if len(nombre)== 0:
                print("el nombre no puede tener 0 caracteres")
            elif len(nombre.strip()) < 8:
                print("porfavor ingreser almenos 8 caracteres")
            else:    
                nombre=input("Ingrese el nombre del paciente?: ")
                prevision=input("Ingrese la prevision del paciente?: ")
                temperatura=float(input("Ingrese la temperatura del paciente?: "))
                pacientes.append({"nombre": nombre,  "prevision": prevision,
                "temperatura": temperatura, "grave": False})
        except ValueError:
            print("se agrego un paciente") 
            print("="*20) 
def actualizar():
    print("i")       
pacientes=[
    {"nombre": " Aquiles Baeza",  "prevision": "fonasa",
     "temperatura": 34.6, "grave": True}, 
    {"nombre": " dON rAMON Baeza",  "prevision": "fonasa",
    "temperatura": 34.6, "grave": False},
    {"nombre": " Señor Barriga",  "prevision": "fonasa",
    "temperatura": 34.6, "grave": False}
]

while True:
    print("""
1.Ingresar pacientes
2.Quitar paciete
3.Tomar Temparatura
4.Mostrar pacientes
5.Salir
""")
    print("="*20)
    op=int(input("seleccione una opcion: "))
    match op:
        case 1:
            agregar()
        case 2:
            borrar()
        case 3:
            actualizar()
        case 4:
            mostrar()
        case 5:
            print("Hasta pronto")
            break  
        case _:
            print("ingrese unaa opcion valida del 1 al 5")