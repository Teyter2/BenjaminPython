import random

# 1. Generar frecuencia objetivo (1 a 100)
frecuencia_objetivo = random.randint(1, 100)

# Pedir frecuencia mínima y máxima al usuario
minimo = int(input("Ingresa frecuencia mínima: "))
maximo = int(input("Ingresa frecuencia máxima: "))

# Validación básica
if minimo >= maximo:
    print("Rango inválido")
    exit()

# 2. Generar frecuencia dentro del rango
frecuencia = random.randint(minimo, maximo)

# Ajuste: múltiplo de 5
if frecuencia % 5 != 0:
    frecuencia += (5 - frecuencia % 5)

# Si se pasa del máximo, restar 1
if frecuencia > maximo:
    frecuencia -= 1

intentos = 3
acertado = False

# 3. Intentos del usuario
while intentos > 0:
    intento = int(input("Adivina la frecuencia calibrada: "))
    
    if intento == frecuencia:
        print("Calibración exitosa")
        acertado = True
        break
    else:
        if intento < frecuencia:
            print("La frecuencia es mayor")
        else:
            print("La frecuencia es menor")
    
    intentos -= 1

# Resultado final
if not acertado:
    print("Calibración fallida")

print("Frecuencia objetivo era:", frecuencia_objetivo)
print("Frecuencia calibrada era:", frecuencia)