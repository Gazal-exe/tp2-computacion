"""
Punto 2: Perfilado de Función Lineal con cProfile
Complejidad Teórica: O(n)
Valores a evaluar según consigna: 12, 20, 30, 40 elementos
"""
import cProfile

def lineal(n):
    total = 0
    for i in range(n):
        total += i
    return total

valores_n = [12, 20, 30, 40]

print("=" * 60)
print("PROFILING: FUNCIÓN LINEAL O(n)")
print("=" * 60)

for n in valores_n:
    print(f"\n--- Función lineal para n = {n} ---")
    cProfile.run("lineal(n)")
