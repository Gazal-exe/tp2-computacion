"""
Punto 1.c: Algoritmo de Optimización - Camino Más Corto (Dijkstra)
Estructura: Cola de prioridad (min-heap con heapq)
Complejidad Teórica:
- Con montículo binario: O((V + E) log V)
  donde V = cantidad de vértices/nodos y E = cantidad de aristas
Tamaños solicitados: 300, 8.000, 70.000, 400.000 y 1.000.000 de nodos
"""
import heapq
import time
import random
import sys

def dijkstra(grafo, inicio):
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[inicio] = 0
    cola_prioridad = [(0, inicio)]
    while cola_prioridad:
        dist_actual, nodo_actual = heapq.heappop(cola_prioridad)
        for vecino, peso in grafo[nodo_actual].items():
            distancia_total = dist_actual + peso
            if distancia_total < distancia[vecino]:
                distancia[vecino] = distancia_total
                heapq.heappush(cola_prioridad, (distancia_total, vecino))
    return distancia

print("=" * 65)
print("PUNTO 1.c: ANÁLISIS DE COMPLEJIDAD - ALGORITMO DE DIJKSTRA")
print("=" * 65)

# Demostración del ejemplo del enunciado
grafo_ejemplo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(f"Demostración inicial desde nodo 'A': {dijkstra(grafo_ejemplo, 'A')}\n")

# Función generadora de grafo disperso conexo (2 aristas por nodo de promedio)
def generar_grafo_disperso(n_nodos):
    grafo = {i: {} for i in range(n_nodos)}
    for i in range(n_nodos):
        vecino_adelante = (i + 1) % n_nodos
        peso = random.randint(1, 100)
        grafo[i][vecino_adelante] = peso
        # Arista de salto largo
        salto = (i + random.randint(2, min(10, n_nodos))) % n_nodos
        if salto not in grafo[i]:
            grafo[i][salto] = random.randint(1, 100)
    return grafo

tamanos = [300, 8000, 70000, 400000, 1000000]

print("Iniciando mediciones empíricas:")
print("-" * 65)
print(f"{'Nodos (V)':<15}{'Aristas aprox (E)':<20}{'Tiempo Dijkstra':<20}")
print("-" * 65)

for v in tamanos:
    if v == 1000000 and "--all" not in sys.argv:
        print(f"{v:<15}{'~2,000,000':<20}{'Omitido (Use --all para correr 1M nodos)':<20}")
        continue
        
    print(f"Construyendo grafo para V={v:,}...", end="\r", flush=True)
    g = generar_grafo_disperso(v)
    aristas = sum(len(vecinos) for vecinos in g.values())
    
    inicio = time.perf_counter()
    distancias = dijkstra(g, 0)
    duracion = time.perf_counter() - inicio
    
    print(f"{v:<15}{f'~{aristas:,}':<20}{f'{duracion:.4f} s':<20}")

print("-" * 65)
print("[CONCLUSIÓN] Al utilizar heapq (min-heap), la complejidad es O((V+E) log V).")
