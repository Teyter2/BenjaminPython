M = 120000
S = 25000

edad = int(input("Ingrese su edad: "))
plan = int(input("""
- Elija un Plan -
1. Basico
2. Pro
3. Elite
"""))

# Inicializar variables para evitar errores
pago_matricula = M
pago_seguro = S

match plan:
    case 1: # Básico
        if edad <= 25:
            pago_matricula = M * 0.90 # 10% dcto
        elif 26 <= edad <= 50:
            pago_matricula = M * 0.95 # 5% dcto
    case 2 | 3: # Pro o Elite
        if edad <= 25:
            pago_matricula = M * 0.80 # 20% dcto
        elif 26 <= edad <= 50:
            pago_matricula = M * 0.85 # 15% dcto

# Lógica del Seguro (Solo para Elite)
if plan == 3:
    if edad > 40:
        pago_seguro = S * 0.40 # 60% dcto
    else:
        pago_seguro = S * 0.50 # 50% dcto

print("\n--- Resumen de Pago ---")
print(f"Plan seleccionado: {plan}")
print(f"Edad del cliente: {edad} años")
print("-" * 25)
print(f"Valor Matrícula: ${pago_matricula:,.0f}")
print(f"Valor Seguro:    ${pago_seguro:,.0f}")
print(f"TOTAL A PAGAR:   ${(pago_matricula + pago_seguro):,.0f}")