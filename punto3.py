"""
PUNTO 3: AJUSTES Y MEJORAS DE RENDIMIENTO
Computación II - TP2 Unidad 3

Se presentan las versiones optimizadas de los algoritmos que presentaron
cuellos de botella en el Punto 2, evaluadas con cProfile:
1. Cuadrática Optimizada: de O(n^2) a O(1)
2. Fibonacci Optimizado (Programación Dinámica): de O(2^n) a O(n)
3. Suma Lineal Optimizada: de O(n) a O(1)
"""

import cProfile
import time
import sys

# Aumentar límite de conversión de enteros gigantes para Fibonacci(100.000+)
sys.set_int_max_str_digits(1_000_000)

print("=" * 70)
print("PUNTO 3: EVALUACIÓN DE ALGORITMOS OPTIMIZADOS (cProfile)")
print("=" * 70)

# =========================================================================
# 1. OPTIMIZACIÓN DE FUNCIÓN CUADRÁTICA: O(n^2) -> O(1)
# =========================================================================
print("\n" + "#" * 70)
print("1. OPTIMIZACIÓN FUNCIÓN CUADRÁTICA: O(n^2) -> O(1)")
print("#" * 70)
print("Fundamentación: La doble sumatoria sum(i * j) equivale a (sum(i))^2.")
print("Aplicando la fórmula de Gauss: sum = ((n - 1) * n // 2) ** 2.")

def cuadratica_optimizada(n):
    suma_gauss = (n - 1) * n // 2
    return suma_gauss * suma_gauss

valores_cuadratica = [10000, 50000, 75000, 200000]

for n in valores_cuadratica:
    print(f"\n--- Cuadrática Optimizada O(1) para n = {n:,} ---")
    cProfile.runctx("cuadratica_optimizada(n)", globals(), locals())

# =========================================================================
# 2. OPTIMIZACIÓN DE FIBONACCI EXPONENCIAL: O(2^n) -> O(n)
# =========================================================================
print("\n" + "#" * 70)
print("2. OPTIMIZACIÓN FIBONACCI: O(2^n) -> O(n) (PROGRAMACIÓN DINÁMICA)")
print("#" * 70)
print("Fundamentación: Se eliminan las llamadas redundantes almacenando")
print("únicamente los dos términos anteriores en variables auxiliares.")

def fibonacci_optimizado(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 2.a) Comparativa directa con los tamaños de Walter (10 a 35)
print("\n[A] Evaluando los mismos tamaños que en Punto 2 (n = 10 a 35):")
for n in [10, 20, 25, 30, 35]:
    print(f"\n--- Fibonacci Optimizado O(n) para n = {n} ---")
    cProfile.runctx("fibonacci_optimizado(n)", globals(), locals())

# 2.b) Tamaños originales de la consigna (que antes daban RecursionError)
print("\n[B] Evaluando los tamaños originales de la consigna (10.000 a 500.000):")
for n in [10000, 100000, 250000, 500000]:
    print(f"\n--- Fibonacci Optimizado O(n) para n = {n:,} ---")
    cProfile.runctx("fibonacci_optimizado(n)", globals(), locals())

# =========================================================================
# 3. OPTIMIZACIÓN DE FUNCIÓN LINEAL: O(n) -> O(1)
# =========================================================================
print("\n" + "#" * 70)
print("3. OPTIMIZACIÓN FUNCIÓN LINEAL: O(n) -> O(1)")
print("#" * 70)

def lineal_optimizada(n):
    return (n - 1) * n // 2

for n in [12, 20, 30, 40, 1_000_000]:
    print(f"\n--- Suma Lineal Optimizada O(1) para n = {n:,} ---")
    cProfile.runctx("lineal_optimizada(n)", globals(), locals())

print("\n" + "=" * 70)
print("FIN DE LA EVALUACIÓN DE MEJORAS")
print("=" * 70)
