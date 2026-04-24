# Ejemplo y explicacion de for

# for i in range(5):
#     print(i+1)

# # Pedir un numero al usuario }
# # mostrar un saludo esa cantidad de veces



# num=int(input("Ingrese un numero: "))
# for i in range(num):
#     print(i+1,"Hola mariano")

# # Pedir un numero al usuario 
# # y mostrar la tabla de multiplicar
# # de ese numero hasta 10.}

# num=int(input("Ingrese un numero: "))

# for i in range(10):
#     print(num, "x" , i+1 , "=", num*(i+1))
#     print(i)

# # for i in range(1,11):
# #     print(num, "x" , i , "=", num*i)

# # Pedir un numero al usuario 
# # y mostrar la suma desde el 1
# # hasta ese numero
# # ej, 3--> 1+2+3=6.

# num=int(input("Ingrese un numero: "))
# suma=0
# for i in range(num):
#     suma=suma+i+1

# print("El resultado de la suma es", suma )

# # Pedir la cantidad de notas al usuario 
# # luego pedir cada nota individualmente
# # calcular el promedio de todas las notas
# # mostrar si aprueba o no

# notas=int(input("Ingrese la cant de notas: "))
# suma=0
# for i in range(notas):
#     n=float(input(f"Ingrese la nota {i+1}: "))
#     suma=suma+n
# prom=suma/notas
# print("El promedio es",round(prom,1) )

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")


# # # cuenta la cantidad de vocales
# nombre=input("Ingrese su nombre: ")
# vocals=0
# conso=0
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU" :
#         vocals+=1
#     elif i ==" ":
#         print("")
#     else:
#         conso+=1

# print("La cantidad de vocales es", vocals)
# print("La cantidad de consonantes es", conso)

# Pida la cantidad de alumnos
# por cada alumno, pida la cantidad 
# de notas. Saque el promedio
# y muestre si aprueba o no
# Muestre la cantidad de alumnos
# apribado sy reprobados.


# num=int(input("Ingrese la cant de alumnos: "))
# apro=0
# repro=0
# for i in range(num):
#     notas=int(input(f"Ingrese la cant de notas del alumno {i+1}: "))
#     suma=0
#     for j in range(notas):
#         n=float(input(f"Ingrese la nota  {j+1}: "))
#         suma=suma+n
#     prom=suma/notas
#     print("El promedio es", prom)

#     if prom>=4:
#         print("ALumno aprobado")
#         apro+=1
#     else:
#         print("ALumno reprobado")
#         repro+=1


# for i in "Diego":
#     print(i)

# Pregunte al usuario su nombre u muestra sus letras
print("Ingrese su nombre")
name=input()
vocales=0
conso=0
#nombre=("INgreses su nombre: ")
for i in name:
    print(i)
    if i in "aeiouAEIOU":
        # vocales=vocales+1
        vocales+=1
    elif i==" ":
        ''''''
    else:
        conso=conso+1
print(f"La cantidad de vocales es {vocales}")
print(f"La cantidad de consocnantes es {conso}")
