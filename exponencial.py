"""
Punto 2: Perfilado de Función Exponencial con cProfile
Algoritmo: Fibonacci Recursivo Ingenuo
Complejidad Teórica: O(2^n)
"""
import cProfile
import sys

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=" * 60)
print("PROFILING: FUNCIÓN EXPONENCIAL O(2^n)")
print("=" * 60)

# 1. Demostración de limitación teórica y técnica con n=10.000 (consigna)
print("\n[TEST 1] Probando n = 10.000 según consigna:")
try:
    cProfile.run("fibonacci(10000)")
except RecursionError as e:
    print(f"-> RecursionError detectado: {e}")
    print("   Explicación: La recursión ingenua supera el límite de pila de Python (1000 llamadas).")
    print("   Además, 2^10000 requeriría más operaciones que la edad del universo.")

# 2. Análisis empírico con tamaños viables
valores_n = [10, 20, 25, 30, 35]
print("\n[TEST 2] Evaluando tamaños viables para registrar tiempos y llamadas:")
for n in valores_n:
    print(f"\n--- Fibonacci para n = {n} ---")
    cProfile.run("fibonacci(n)")
