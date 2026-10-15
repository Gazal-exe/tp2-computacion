import cProfile

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

valores_n = [10, 20, 25, 30, 35]

for n in valores_n:
    print(f"\n--- Fibonacci para n = {n} ---")
    cProfile.run(
        "fibonacci(n)"
    )
# lineal:
import cProfile
def lineal(n):
    total = 0
    for i in range(n):
        total += i
    return total

valores_n = [12, 20 , 30, 40]
for n in valores_n:
    print(f"\n--- Función lineal para n = {n} ---")
    cProfile.run("lineal(n)") 
import cProfile

def cuadratica(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

valores_n=[10000, 50000, 75000, 200000]

for n in valores_n:
    print(f"\n--- Función cuadratica para n = {n} ---")
    cProfile.run("cuadratica(n)")
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