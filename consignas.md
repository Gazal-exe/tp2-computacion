# Trabajo Práctico 2 - Unidad 3: Evaluación de Complejidad y Optimización

## Objetivos
El objetivo de este trabajo práctico es analizar la complejidad de un algoritmo, identificar cuellos de botella en el código y realizar ajustes y mejoras basadas en el perfilado.

---

## Consignas

### 1. Análisis de Complejidad
Realiza un análisis de complejidad para un algoritmo dado. Debes considerar los siguientes casos:

#### 1.a) Ordenamiento por burbujas (Bubble Sort)
Aplicar el análisis de complejidad. Realizar para **300**, **8.000**, **70.000**, **400.000** y **1.000.000** de elementos.
Este algoritmo es uno de los métodos más simples para ordenar una lista.

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numeros))
```

#### 1.b) Ordenamiento rápido (Quick Sort)
Aplicar el análisis de complejidad. Realizar para **300**, **8.000**, **70.000**, **400.000** y **1.000.000** de elementos.
Un algoritmo eficiente para ordenar listas que utiliza la técnica de divide y vencerás.

```python
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(numeros))
```

#### 1.c) Algoritmo de optimización (Dijkstra)
Aplicar el análisis de complejidad. Realizar para **300**, **8.000**, **70.000**, **400.000** y **1.000.000** de elementos.
Utilizado para encontrar el camino más corto en un grafo ponderado.

```python
import heapq

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

# Uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(grafo, 'A'))
```

#### 1.d) Algoritmo de procesamiento de datos (Filtrado / Filter)
Aplicar el análisis de complejidad.
Realizar para **300**, **1.000**, **50.000** y **300.000** elementos, un filtrado de números pares e impares.
Un algoritmo que permite filtrar elementos de una lista según una condición.

```python
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_pares(numeros))
```

---

### 2. Identificación de Cuellos de Botella
- Teniendo en cuenta el código del TP anterior y utilizando herramientas de análisis de rendimiento (como profilers) para identificar las partes del código que consumen más recursos (tiempo y memoria).
- Documenta los cuellos de botella encontrados y proporciona ejemplos específicos del código que los generan.
- El código a analizar es:
  - **Función Lineal**: (12, 20, 30 y 40 elementos)
  - **Función Exponencial**: (10.000, 100.000, 250.000 y 500.000 elementos)
  - **Función Logarítmica**: (20.000, 50.000, 100.000 y 250.000 elementos)
  - **Función Polinómica**: (10.000, 50.000, 75.000 y 200.000 elementos)

#### Ejemplo de Profiler en Python – Para suma lineal:
```python
import cProfile

def suma_lineal(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma

# Usando cProfile para analizar la función
cProfile.run('suma_lineal(1000000)')
```

**Resultado de ejemplo:**
```text
         4 function calls in 0.245 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.245    0.245 <ipython-input-...>:3(suma_lineal)
        1    0.000    0.000    0.245    0.245 <string>:1(<module>)
        1    0.245    0.245    0.245    0.245 {built-in method builtins.exec}
        1    0.000    0.000    0.245    0.245 <string>:1(<module>)
```

**Análisis de Resultados:**
- `ncalls`: Número de llamadas a la función.
- `tottime`: Tiempo total gastado en la función sin incluir llamadas a otras funciones.
- `cumtime`: Tiempo acumulado, incluye el tiempo en la función y en las funciones que llamó.

**Cuello de botella:**
- **Cuello de Botella Potencial**: En este caso, el cuello de botella está relacionado con la complejidad O(n) del algoritmo. A medida que n crece, el tiempo de ejecución aumentará linealmente. Para valores muy grandes de n, el tiempo de ejecución puede volverse inaceptable.
- **Optimización**: En lugar de usar un bucle para sumar los números, podrías utilizar la fórmula matemática de la suma de los primeros n números: `suma = n * (n - 1) // 2`. Esto reduce la complejidad a O(1), eliminando el cuello de botella.

---

### 3. Ajustes y Mejoras
- Proporciona soluciones o ajustes que podrían mejorar el rendimiento del algoritmo. Esto puede incluir:
  - Cambios en la estructura de datos utilizada.
  - Implementación de algoritmos más eficientes, explique el motivo de por qué y fundamente.
  - Optimización de bucles o condiciones.
- Realiza una nueva evaluación de la complejidad después de aplicar las mejoras, y compara los resultados con los análisis previos.

---

## Entregables
Un informe que contenga:
- Análisis de complejidad (mejor caso, caso promedio y peor caso). (Punto 1)
- Identificación de cuellos de botella con ejemplos de código. (Punto 2)
- Propuestas de mejoras y análisis de la nueva complejidad. (Punto 3)
- Código fuente del algoritmo original y del algoritmo optimizado. (Punto 3)

## Criterios de Evaluación
- Claridad y precisión en el análisis de complejidad.
- Identificación efectiva de cuellos de botella.
- Originalidad y efectividad de las mejoras propuestas.
- Calidad del informe y del código presentado.

## Fecha de Entrega
- **Fecha de entrega:** 16/10/2026 – Por plataforma y sólo un integrante lo debe subir.
