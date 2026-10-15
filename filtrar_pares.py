"""
Punto 1.d: Algoritmo de Procesamiento de Datos - Filtrado (Filter)
Función: Filtrado de números pares en una lista
Complejidad Teórica:
- Mejor caso: O(n)
- Caso promedio: O(n)
- Peor caso: O(n)
(Recorre una sola vez cada elemento aplicando la condición lambda x: x % 2 == 0)
Tamaños solicitados: 300, 1.000, 50.000 y 300.000 elementos
"""
import random
import time

def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

print("=" * 65)
print("PUNTO 1.d: ANÁLISIS DE COMPLEJIDAD - FILTRADO (FILTER)")
print("=" * 65)

# Demostración del enunciado
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Demostración inicial: {filtrar_pares(numeros)}\n")

# Tamaños solicitados
tamanos = [300, 1000, 50000, 300000]

print("Iniciando mediciones empíricas:")
print("-" * 65)
print(f"{'Tamaño (N)':<15}{'Complejidad Teórica':<25}{'Tiempo (segundos)':<20}")
print("-" * 65)

for n in tamanos:
    datos = [random.randint(1, 1_000_000) for _ in range(n)]
    inicio = time.perf_counter()
    pares = filtrar_pares(datos)
    duracion = time.perf_counter() - inicio
    print(f"{n:<15}{'O(n) [lineal]':<25}{f'{duracion:.6f} s':<20}")

print("-" * 65)
print("[CONCLUSIÓN] La función filter() recorre la lista en una sola pasada O(n).")
