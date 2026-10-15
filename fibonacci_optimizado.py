import cProfile
import sys

# Ajuste para soportar enteros con más de 4300 dígitos (necesario para n >= 10000)
sys.set_int_max_str_digits(1_000_000)

def fibonacci_optimizado(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Prueba con los valores del análisis previo (n <= 35)
valores_previos = [10, 20, 25, 30, 35]
print("=== COMPARATIVA CON ANÁLISIS PREVIO ===")
for n in valores_previos:
    print(f"\n--- Fibonacci optimizado para n = {n} ---")
    cProfile.run("fibonacci_optimizado(n)")

# Prueba con los tamaños grandes de la consigna (que antes daban RecursionError)
valores_consigna = [10000, 100000, 250000, 500000]
print("\n=== EVALUACIÓN CON TAMAÑOS DE LA CONSIGNA (ANTES INVIABLES) ===")
for n in valores_consigna:
    print(f"\n--- Fibonacci optimizado para n = {n} ---")
    cProfile.run("fibonacci_optimizado(n)")
