# Datos de entrada
capital = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
tiempo = float(input("Ingrese el tiempo en años: "))

# Cálculo de interés compuesto
interes_compuesto = capital * (1 + tasa_interes / 100) ** tiempo - capital

# Resultado
print(f"El interés compuesto después de {tiempo} años es: {interes_compuesto:.2f}")
