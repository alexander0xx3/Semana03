# Función para convertir calificación numérica a literal
def calificacion_literal(calificacion):
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"

# Leer calificación numérica
calificacion = float(input("Ingrese la calificación numérica: "))

# Convertir a calificación literal
calif_literal = calificacion_literal(calificacion)

# Imprimir resultado
print(f"La calificación literal es: {calif_literal}")
