import math

# Convertir grados a radianes
grados = float(input("Ingrese el ángulo en grados: "))
radianes = math.radians(grados)
print(f"{grados} grados son {radianes:.4f} radianes")

# Convertir radianes a grados
radianes = float(input("Ingrese el ángulo en radianes: "))
grados = math.degrees(radianes)
print(f"{radianes:.4f} radianes son {grados:.4f} grados")
