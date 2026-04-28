from typing import Match

def verificar_tipo(valor: Match )-> str:
    match valor:
        case 1:
            return "es un numero entero"
        case "texto":
            return "es una cadena de texto"
        case 3.14:
            return "es un numero decimal"
        case _:
            return "tipo no reconocido"

resultado = verificar_tipo(10)
print(resultado)