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
    print("el nombre del producto es:",productos[1]["precio"])
    print("el nombre del producto es:",productos[2]["precio"])
    print("el nombre del producto es:",productos[3]["precio"])
    print("="*20)
productos={
    1:{"nombre":"leche", "precio":1200},
    2:{"nombre":"mani", "precio":1600},
    3:{"nombre":"cereal", "precio":3200}
}

while True:
    print("""
1.Agregar juego
2.Borrar juego
3.Actualizar juego
4.Mostrar juegos
5.Salir
""")
    print("="*20)
    op=int(input("seleccione una opcion: "))
    match op:
        case 1:
            mostrar()
