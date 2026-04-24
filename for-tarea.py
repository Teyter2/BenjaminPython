#for tarea
# for i in range(5):
#     print(i+1)
# num=int(input("ingrese un numero "))
# for i in range(num):
#     print("repeticion ", i+1)

# print("ingrese un numero para multiplicar")
# num=int(input("numero "))
# for i in range(1,10+1):
#     print(num,"x",i,"=",num*i)

print("-NOTAS-")
ap=0
re=0
num=int(input("Ingrese cantidad de alumnos: "))
for a in range(num):
    notas=int(input(f"Ingrese la cantidad de notas {a+1}: "))
    suma=0
    for o in range(notas):
        n=float(input(f"Ingrese la nota  {o+1}: "))
        suma=suma+n
    prom=suma/notas
    print("El promedio es", prom)
    if prom>=4:
        print("Alumno aprobado")
        ap+=1
    else:
        print("Alumno reprobado")
        re+=1