import cProfile

def lineal_optimizada(n):
    # Fórmula de Gauss: suma de 0 a n-1
    return (n - 1) * n // 2

valores_n = [12, 20, 30, 40, 1000000]

for n in valores_n:
    print(f"\n--- Función lineal optimizada O(1) para n = {n} ---")
    cProfile.run("lineal_optimizada(n)")
