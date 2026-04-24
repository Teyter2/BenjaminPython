import turtle

# Crear el lienzo y nuestro lápiz (la tortuga)
ventana = turtle.Screen()
lapiz = turtle.Turtle()

# Hacer que el lápiz sea un poco más grueso
lapiz.pensize(3)

# Ciclo para dibujar los 4 lados del cuadrado
for i in range(80):
    lapiz.forward(100)  # Avanza 100 píxeles dibujando una línea
    lapiz.right(260) # Gira 90 grados a la derecha
# Mantener la ventana abierta hasta que el usuario haga clic en ella
ventana.exitonclick()