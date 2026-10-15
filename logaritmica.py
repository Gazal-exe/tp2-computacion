"""
Punto 2: Perfilado de Función Logarítmica con cProfile
Complejidad Teórica: O(log n)
Valores a evaluar según consigna: 20000, 50000, 100000, 250000 elementos
"""
import cProfile

def logaritmica(n):
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
    return total

valores_n = [20000, 50000, 100000, 250000]

print("=" * 60)
print("PROFILING: FUNCIÓN LOGARÍTMICA O(log n)")
print("=" * 60)

for n in valores_n:
    print(f"\n--- Función logarítmica para n = {n} ---")
    cProfile.run("logaritmica(n)")
