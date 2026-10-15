"""
Punto 1.b: Ordenamiento Rápido (Quick Sort)
Técnica: Divide y Vencerás
Complejidad Teórica:
- Mejor caso: O(n log n)
- Caso promedio: O(n log n)
- Peor caso: O(n^2) (si los pivotes son extremadamente desbalanceados)
Tamaños solicitados: 300, 8.000, 70.000, 400.000 y 1.000.000 de elementos
"""
import random
import time
import sys

# Ajustar límite de recursión para soportar listas de hasta 1 millón de elementos
sys.setrecursionlimit(2_000_000)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

print("=" * 65)
print("PUNTO 1.b: ANÁLISIS DE COMPLEJIDAD - QUICK SORT")
print("=" * 65)

# Demostración inicial
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Demostración inicial: {quick_sort(numeros)}\n")

# Tamaños solicitados
tamanos = [300, 8000, 70000, 400000, 1000000]

print("Iniciando mediciones empíricas:")
print("-" * 65)
print(f"{'Tamaño (N)':<15}{'Operaciones O(n log n)':<25}{'Tiempo (segundos)':<20}")
print("-" * 65)

for n in tamanos:
    # Generar lista de números aleatorios
    datos = [random.randint(1, 10_000_000) for _ in range(n)]
    
    inicio = time.perf_counter()
    resultado = quick_sort(datos)
    duracion = time.perf_counter() - inicio
    
    import math
    ops = int(n * math.log2(n))
    print(f"{n:<15}{f'~{ops:,}':<25}{f'{duracion:.4f} s':<20}")

print("-" * 65)
print("[CONCLUSIÓN] Quick Sort escala de forma logarítmica-lineal O(n log n),")
print("             ordenando 1 millón de elementos en apenas unos pocos segundos.")
