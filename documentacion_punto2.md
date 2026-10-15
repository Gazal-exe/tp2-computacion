# Punto 2: Identificación de Cuellos de Botella mediante Profiling

**Responsable:** Walter
**Herramienta utilizada:** `cProfile` (módulo estándar de Python)

---

## 1. Función Lineal: $O(n)$

### Código analizado
```python
import cProfile

def lineal(n):
    total = 0
    for i in range(n):
        total += i
    return total

valores_n = [12, 20, 30, 40]
for n in valores_n:
    print(f"\n--- Función lineal para n = {n} ---")
    cProfile.run("lineal(n)")
```

### Resultados obtenidos con cProfile

| Tamaño ($n$) | Llamadas (`ncalls`) | Tiempo total (`tottime`) | Tiempo acumulado (`cumtime`) | Función |
| :---: | :---: | :---: | :---: | :--- |
| **12** | 1 | 0.000 s | 0.000 s | `ejercicio2Lineal.py:3(lineal)` |
| **20** | 1 | 0.000 s | 0.000 s | `ejercicio2Lineal.py:3(lineal)` |
| **30** | 1 | 0.000 s | 0.000 s | `ejercicio2Lineal.py:3(lineal)` |
| **40** | 1 | 0.000 s | 0.000 s | `ejercicio2Lineal.py:3(lineal)` |

### Análisis de Cuello de Botella
- Para valores pequeños de $n$ ($12 \le n \le 40$), el tiempo de ejecución es prácticamente imperceptible ($< 1$ ms) y no representa ningún cuello de botella.
- No obstante, la complejidad es $O(n)$, lo cual implica que para valores muy grandes de $n$ el tiempo crecerá linealmente.

---

## 2. Función Logarítmica: $O(\log n)$

### Código analizado
```python
import cProfile

def logaritmica(n):
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
    return total

valores_n = [20000, 50000, 100000, 250000]
for n in valores_n:
    print(f"\n--- Función logarítmica para n = {n} ---")
    cProfile.run("logaritmica(n)")
```

### Resultados obtenidos con cProfile

| Tamaño ($n$) | Llamadas (`ncalls`) | Iteraciones del bucle ($\approx \log_2 n$) | Tiempo total (`tottime`) | Tiempo acumulado (`cumtime`) | Función |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **20.000** | 1 | 15 iteraciones | 0.000 s | 0.000 s | `ejercicio2Logaritmica.py:5(logaritmica)` |
| **50.000** | 1 | 16 iteraciones | 0.000 s | 0.000 s | `ejercicio2Logaritmica.py:5(logaritmica)` |
| **100.000** | 1 | 17 iteraciones | 0.000 s | 0.000 s | `ejercicio2Logaritmica.py:5(logaritmica)` |
| **250.000** | 1 | 18 iteraciones | 0.000 s | 0.000 s | `ejercicio2Logaritmica.py:5(logaritmica)` |

### Análisis de Cuello de Botella
- El crecimiento es extremadamente lento ($O(\log n)$). Multiplicar el tamaño de entrada por más de 10 apenas agrega unas pocas iteraciones.
- La función es altamente escalable y no presenta cuellos de botella para estos volúmenes.

---

## 3. Función Cuadrática / Polinómica: $O(n^2)$

### Código analizado
```python
import cProfile

def cuadratica(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

valores_n = [10000, 50000, 75000, 200000]
for n in valores_n:
    print(f"\n--- Función cuadrática para n = {n} ---")
    cProfile.run("cuadratica(n)")
```

### Resultados obtenidos con cProfile

| Tamaño ($n$) | Iteraciones ($n^2$) | Tiempo total (`tottime`) | Tiempo acumulado (`cumtime`) | Factor de incremento temporal |
| :---: | :---: | :---: | :---: | :---: |
| **10.000** | $10^8$ (100 millones) | **4.017 s** | **4.017 s** | Base ($1\times$) |
| **50.000** | $2.5 \times 10^9$ (2.500 millones) | **114.306 s** (~1.9 min) | **114.306 s** | $\approx 28.5\times$ (teórico: $25\times$) |
| **75.000** | $5.625 \times 10^9$ (5.625 millones) | **293.100 s** (~4.9 min) | **293.100 s** | $\approx 73\times$ (teórico: $56.25\times$) |
| **200.000** | $4 \times 10^{10}$ (40.000 millones) | **1953.828 s** (~32.6 min) | **1953.828 s** | $\approx 486\times$ (teórico: $400\times$) |

### Identificación de Cuello de Botella Crítico
- **Localización:** El bucle anidado interno (`for j in range(n)` dentro de `for i in range(n)`).
- **Evidencia del Profiler:** El 100% del tiempo de CPU (`tottime = 1953.828s`) se consume en la función `cuadratica`.
- **Impacto:** Con $n=200.000$, la ejecución requirió más de **32 minutos**. Para cualquier sistema en producción, esto es inaceptable e inviable.

---

## 4. Función Exponencial: $O(2^n)$ (Fibonacci Recursivo Ingenuo)

### Código analizado
```python
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Intento con los tamaños originales de la consigna ($n = 10.000$)
Al ejecutar con $n = 10.000$:
- La ejecución finalizó inmediatamente con un **`RecursionError: maximum recursion depth exceeded`**.
- **Causa:** Python impone un límite de profundidad en la pila de llamadas (por defecto 1.000 llamadas). La recursión ingenua sobrepasa este límite antes de poder si quiera avanzar en el árbol de cálculo.
- **Conclusión metodológica:** Los tamaños de la consigna ($10.000, 100.000, 250.000, 500.000$) son inviables para un algoritmo exponencial recursivo, tanto por desbordamiento de pila (*stack overflow*) como por tiempo de ejecución ($2^{10000}$ operaciones supera la capacidad del universo observable).

### Análisis empírico con valores viables ($n \in [10, 20, 25, 30, 35]$)

| Tamaño ($n$) | Llamadas a función (`ncalls`) | Llamadas primitivas | Tiempo total (`cumtime`) | Crecimiento de llamadas |
| :---: | :---: | :---: | :---: | :---: |
| **10** | 177 | 1 | **0.000 s** | - |
| **20** | 21.891 | 1 | **0.004 s** | $\approx 123\times$ |
| **25** | 242.785 | 1 | **0.042 s** | $\approx 11\times$ |
| **30** | 2.692.537 | 1 | **0.472 s** | $\approx 11.1\times$ |
| **35** | 29.860.703 | 1 | **5.335 s** | $\approx 11.1\times$ |

### Identificación de Cuello de Botella Crítico
- **Localización:** La bifurcación recursiva no memoizada `fibonacci(n - 1) + fibonacci(n - 2)`.
- **Evidencia del Profiler:** Para apenas $n=35$, el profiler registra casi **30 millones de llamadas a funciones** (`29.860.703 ncalls`).
- **Naturaleza del problema:** Se recalculan exponencialmente los mismos subproblemas una y otra vez (por ejemplo, `fibonacci(2)` se calcula millones de veces).
