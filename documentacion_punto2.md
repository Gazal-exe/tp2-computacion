# Punto 2: Identificación de Cuellos de Botella mediante Profiling

**Responsable:** Walter
**Herramienta utilizada:** `cProfile` (módulo estándar de Python)

---

## 1. Función Cuadrática $O(n^2)$

### Descripción y Código Analizado
Para identificar los cuellos de botella de la función cuadrática, se utilizó la herramienta `cProfile` de Python. Las pruebas se realizaron con tamaños de entrada de **10.000**, **50.000**, **75.000** y **200.000** elementos.

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

### Identificación del Cuello de Botella
El código analizado contiene dos bucles anidados. El bucle exterior recorre los valores de `i`, mientras que el interior recorre los valores de `j` para cada iteración del exterior. Dentro del bucle interior se ejecuta la operación `total += i * j`, que realiza una multiplicación y acumula su resultado.

El **principal cuello de botella** se encuentra en la **ejecución repetida del bucle interior**. Como ambos bucles realizan $n$ iteraciones, el cuerpo del bucle interior se ejecuta $n^2$ veces. Por este motivo, la complejidad temporal de la función es $O(n^2)$.

### Resultados obtenidos con cProfile

| Tamaño ($n$) | Iteraciones del bucle ($n^2$) | Tiempo total (`tottime`) | Tiempo acumulado (`cumtime`) | Incremento temporal observado |
| :---: | :---: | :---: | :---: | :---: |
| **10.000** | $10^8$ (100 millones) | **4,017 s** | **4,017 s** | Base ($1\times$) |
| **50.000** | $2.5 \times 10^9$ (2.500 millones) | **114,306 s** (~1,9 min) | **114,306 s** | $\approx 28,46\times$ (teórico: $25\times$) |
| **75.000** | $5.625 \times 10^9$ (5.625 millones) | **293,100 s** (~4,9 min) | **293,100 s** | $\approx 72,96\times$ (teórico: $56,25\times$) |
| **200.000** | $4 \times 10^{10}$ (40.000 millones) | **1.953,828 s** (~32,56 min) | **1.953,828 s** | $\approx 486,39\times$ (teórico: $400\times$) |

### Conclusión de Cuello de Botella
Los resultados muestran un incremento considerable del tiempo de ejecución a medida que aumenta el tamaño de entrada. Por ejemplo, al multiplicar $n$ por cinco, pasando de 10.000 a 50.000, el tiempo de ejecución aumentó aproximadamente **28,46 veces**. Este resultado es muy cercano al aumento de 25 veces que se esperaría teóricamente para una función cuadrática ($5^2 = 25$).

En conclusión, las mediciones respaldan el comportamiento cuadrático del algoritmo. El cuello de botella se debe principalmente a la **gran cantidad de iteraciones de los bucles anidados**, que provoca que el tiempo de ejecución aumente considerablemente para entradas grandes.

---

## 2. Función Exponencial: Fibonacci Recursivo $O(2^n)$

### Descripción y Código Analizado
Para analizar el comportamiento exponencial, se utilizó una implementación recursiva de Fibonacci sin optimizaciones. Las pruebas se realizaron con valores de entrada de **10, 20, 25, 30 y 35**, utilizando `cProfile` para registrar las llamadas a funciones y sus tiempos de ejecución.

```python
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

valores_n = [10, 20, 25, 30, 35]
for n in valores_n:
    print(f"\n--- Fibonacci para n = {n} ---")
    cProfile.run("fibonacci(n)")
```

### Identificación del Cuello de Botella
El **principal cuello de botella** se encuentra en la instrucción:
```python
return fibonacci(n - 1) + fibonacci(n - 2)
```
Esta instrucción genera **dos llamadas recursivas** por cada llamada que no alcanza un caso base. Como la función no almacena los resultados calculados anteriormente, vuelve a realizar cálculos que ya se habían efectuado en otras ramas de la recursión (subproblemas superpuestos).

### Resultados obtenidos con cProfile

| Tamaño ($n$) | Invocaciones a funciones (`ncalls`) | Llamadas primitivas | Tiempo de ejecución (`cumtime`) | Incremento temporal |
| :---: | :---: | :---: | :---: | :---: |
| **10** | 177 | 1 | **0,000 s** | - |
| **20** | 21.894 | 1 | **0,004 s** | - |
| **25** | 242.788 | 1 | **0,042 s** | $\approx 10,5\times$ |
| **30** | 2.692.540 | 1 | **0,472 s** | $\approx 11,2\times$ |
| **35** | 29.860.706 | 1 | **5,335 s** | $\approx 11,3\times$ |

### Limitación Técnica y Conclusión
Al aumentar $n$ de 30 a 35, el tiempo de ejecución creció aproximadamente **11,3 veces**. Este comportamiento evidencia que el costo computacional aumenta rápidamente incluso ante incrementos relativamente pequeños del tamaño de entrada.

La implementación presenta complejidad temporal exponencial, habitualmente expresada mediante la cota superior $O(2^n)$ (asintóticamente $O(\phi^n)$ con $\phi \approx 1,618$). Su principal limitación es la repetición de cálculos debido a las llamadas recursivas redundantes.

Al intentar ejecutar la función con $n = 10.000$, se produjo un **`RecursionError`**, debido a que se superó el límite de profundidad de recursión de Python (`sys.getrecursionlimit()`). Además de esta limitación de pila, el crecimiento exponencial hace que el cálculo resulte inviable para valores de entrada tan grandes ($2^{10000}$ operaciones).

En conclusión, el principal cuello de botella de esta implementación es la cantidad de llamadas recursivas que repiten cálculos ya realizados. Las mediciones obtenidas respaldan el crecimiento exponencial del trabajo y muestran por qué esta solución resulta poco eficiente para valores grandes de $n$.

---

## 3. Función Lineal y Función Logarítmica

* **Función Lineal ($n \in [12, 20, 30, 40]$):**
  * Tiempos registrados: $0,000\text{ s}$ en todos los casos.
  * Al tratarse de valores muy reducidos de $n$, no existe impacto apreciable en la CPU, aunque la complejidad $O(n)$ escalará linealmente si $n$ crece a millones de elementos.

* **Función Logarítmica ($n \in [20.000, 50.000, 100.000, 250.000]$):**
  * Tiempos registrados: $0,000\text{ s}$ en todos los casos.
  * Para $n = 250.000$, el bucle apenas itera 18 veces ($\log_2 250.000 \approx 17,9$), demostrando una eficiencia óptima sin cuellos de botella detectables.
