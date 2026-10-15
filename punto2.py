"""
Punto 2: Identificación de Cuellos de Botella con cProfile
Computación II - TP2 Unidad 3

Funciones analizadas:
- lineal(n)
- logaritmica(n)
- cuadratica(n) [polinómica]
- fibonacci(n) [exponencial]
"""

import cProfile
import sys

# -------------------------------------------------------------
# 1. Función Lineal: O(n)
# -------------------------------------------------------------
def lineal(n):
    total = 0
    for i in range(n):
        total += i
    return total

def ejecutar_lineal():
    print("\n" + "=" * 50)
    print("EJECUCIÓN: Función Lineal O(n)")
    print("=" * 50)
    valores_n = [12, 20, 30, 40]
    for n in valores_n:
        print(f"\n--- Función lineal para n = {n} ---")
        cProfile.runctx("lineal(n)", globals(), locals())

# -------------------------------------------------------------
# 2. Función Logarítmica: O(log n)
# -------------------------------------------------------------
def logaritmica(n):
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
    return total

def ejecutar_logaritmica():
    print("\n" + "=" * 50)
    print("EJECUCIÓN: Función Logarítmica O(log n)")
    print("=" * 50)
    valores_n = [20000, 50000, 100000, 250000]
    for n in valores_n:
        print(f"\n--- Función logarítmica para n = {n} ---")
        cProfile.runctx("logaritmica(n)", globals(), locals())

# -------------------------------------------------------------
# 3. Función Cuadrática / Polinómica: O(n^2)
# -------------------------------------------------------------
def cuadratica(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

def ejecutar_cuadratica(ejecutar_pesados=False):
    print("\n" + "=" * 50)
    print("EJECUCIÓN: Función Cuadrática O(n^2)")
    print("=" * 50)
    
    # n=10000 toma ~4 seg. Tamaños mayores (50k, 75k, 200k) toman minutos/horas.
    valores_n = [10000]
    if ejecutar_pesados:
        valores_n = [10000, 50000, 75000, 200000]
        
    for n in valores_n:
        print(f"\n--- Función cuadrática para n = {n} ---")
        cProfile.runctx("cuadratica(n)", globals(), locals())
        
    if not ejecutar_pesados:
        print("\n[INFO] Para ejecutar n=[50000, 75000, 200000] (puede tardar más de 35 min en total),")
        print("       ejecute pasando el argumento '--all-quad'.")

# -------------------------------------------------------------
# 4. Función Exponencial (Fibonacci recursivo ingenuo): O(2^n)
# -------------------------------------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def ejecutar_exponencial():
    print("\n" + "=" * 50)
    print("EJECUCIÓN: Función Exponencial O(2^n)")
    print("=" * 50)
    
    # Demostración del RecursionError con n=10000 solicitado por la consigna
    print("\nProbando n = 10000 según consigna (supera el límite de recursión de Python):")
    try:
        cProfile.runctx("fibonacci(10000)", globals(), locals())
    except RecursionError as e:
        print(f"-> RecursionError capturado con éxito: {e}")
        print("   Explicación: La recursión ingenua supera el límite de profundidad (sys.getrecursionlimit() = 1000).")
    
    # Análisis empírico con valores viables
    valores_n = [10, 20, 25, 30, 35]
    print("\nEjecución con valores de n viables para el análisis empírico:")
    for n in valores_n:
        print(f"\n--- Fibonacci para n = {n} ---")
        cProfile.runctx("fibonacci(n)", globals(), locals())

if __name__ == "__main__":
    todos_los_cuadraticos = "--all-quad" in sys.argv
    ejecutar_lineal()
    ejecutar_logaritmica()
    ejecutar_cuadratica(ejecutar_pesados=todos_los_cuadraticos)
    ejecutar_exponencial()
