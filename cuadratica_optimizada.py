import cProfile

def cuadratica_optimizada(n):
    # La sumatoria doble equivale a (suma_gauss)^2
    suma = (n - 1) * n // 2
    return suma * suma

valores_n = [10000, 50000, 75000, 200000]

for n in valores_n:
    print(f"\n--- Función cuadrática optimizada O(1) para n = {n} ---")
    cProfile.run("cuadratica_optimizada(n)")
