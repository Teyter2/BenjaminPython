# juegos={
#     "nombre del juego:": "clach of clans",
#     "tipo de juego:": "crear un pueblo",
#     "publico de edad:": 10,
#     "año": 2008
# }
# def mostrar():
#     for i, a in juegos.items():
#         print(i, a)
#     print("="*20)
# def agregar():
#     i=int(input("que juego quiere agregar? "))
# def borrar():
#         mostrar()
#         eliminar=input("que juego quiere borrar? ")
#         del juegos[eliminar]
# # for i, a in juegos.items():
# #     print(i, a)

# # print(juegos["publico de edad:"])
# # G=int(input("ingrese mas edad para el juego"))
# # juegos["publico de edad:"]=G
# while True:
#     print("1.Agregar juego")
#     print("2.Borrar juego")
#     print("3.Actualizar juego")
#     print("4.Mostrar juegos")
#     print("5.Salir")
#     print("="*20)
#     op=int(input("elija una opcion: "))
#     match op:
#         case 1:
#             agregar()
#         case 2:
#             borrar()
#         case 3:
#             mostrar()
#         case 4:
#             mostrar()
#         case 5:
#                 print("Gracias por usar")
#                 break                    
def mostrar():
    for d,p in productos.items():
        print(f"{d}: nombre:{p["nombre"]}  precio:{p["precio"]}")
    print("="*20)
def agregar():
    nombre=input("Que producto quiere agregar?: ")
    precio=int(input("cual es el precio del producto?: "))
    if productos:
        datonuevo = max(productos.keys()) + 1
    else:
        datonuevo = 1
    productos[datonuevo] = {"nombre": nombre, "precio": precio}
    print("se agrego un nuevo producto")
    print("="*20)
def borrar():
    try:
        mostrar()
        eliminar=int(input("que producto quiere borrar: "))
        del productos[eliminar]
        print("producto borrado")
    except ValueError:
        print("eliga una opcion numerica")
def actualizar():
    if not productos:
        print("No hay productos para actualizar")
        return
    mostrar()
    try:
        actualizar = int(input("¿Qué producto quiere actualizar?: "))

        if actualizar in productos:
            print(f"Actualizando: {productos[actualizar]['nombre']}")
            nuevonombre = input("Nuevo nombre (Enter para no cambiar): ")
            if nuevonombre:
                productos[actualizar]["nombre"] = nuevonombre
            nuevoprecio = input("Nuevo precio (Enter para no cambiar): ")
            if nuevoprecio:
                productos[actualizar]["precio"] = int(nuevoprecio)
            print("Producto actualizado")
        else:
            print("Ese producto no existe")
    except ValueError:
        print("Por favor, ingrese un número válido")
productos={
    1:{"nombre":"leche", "precio":1200},
    2:{"nombre":"mani", "precio":1600},
    3:{"nombre":"cereal", "precio":3200}
}
while True:
    print("""
1.Agregar producto
2.Borrar producto
3.Actualizar producto
4.Mostrar producto
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