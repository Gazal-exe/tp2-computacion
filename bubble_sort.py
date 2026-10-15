"""
Punto 1.a: Ordenamiento por Burbujas (Bubble Sort)
Complejidad Teórica:
- Mejor caso: O(n) (si está optimizado con bandera) u O(n^2) (versión ingenua)
- Caso promedio: O(n^2)
- Peor caso: O(n^2)
Tamaños solicitados: 300, 8.000, 70.000, 400.000 y 1.000.000 de elementos
"""
import random
import time
import sys

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("=" * 65)
print("PUNTO 1.a: ANÁLISIS DE COMPLEJIDAD - BUBBLE SORT")
print("=" * 65)

# Ejemplo básico de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Demostración inicial: {bubble_sort(numeros[:])}\n")

# Tamaños solicitados
tamanos = [300, 8000, 70000, 400000, 1000000]

print("Iniciando mediciones empíricas:")
print("-" * 65)
print(f"{'Tamaño (N)':<15}{'Iteraciones Teóricas O(n^2)':<30}{'Tiempo (segundos)':<20}")
print("-" * 65)

for n in tamanos:
    # Para n >= 70000 en Python puro, O(n^2) toma minutos u horas
    if n > 8000 and "--all" not in sys.argv:
        print(f"{n:<15}{f'~{n**2//2:,}':<30}{'Omitido (Use --all para correr >2 min)':<20}")
        continue
    elif n > 70000 and "--force-huge" not in sys.argv:
        print(f"{n:<15}{f'~{n**2//2:,}':<30}{'Omitido (>1 hora requerida para O(n^2))':<20}")
        continue

    datos = [random.randint(1, 10_000_000) for _ in range(n)]
    inicio = time.perf_counter()
    bubble_sort(datos)
    duracion = time.perf_counter() - inicio
    print(f"{n:<15}{f'~{n**2//2:,}':<30}{f'{duracion:.4f} s':<20}")

print("-" * 65)
print("[INFO] Bubble Sort con n=8.000 realiza ~32 millones de comparaciones.")
print("       Con n=70.000 realiza ~2.450 millones de comparaciones (~2 a 3 min).")
print("       Con n=1.000.000 realizaría ~500.000 millones de operaciones (~días).")
