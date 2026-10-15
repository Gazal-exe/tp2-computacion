
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