import numpy as np

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    # Generar arrays aleatorios usando NumPy
    a = np.random.randint(10, size=5)
    b = np.random.randint(10, size=5)
    c = np.zeros(5, dtype=int)  # Array para almacenar resultados

    # Ejecutar la función worker secuencialmente
    for tid in range(5):
        worker(tid, a, b, c)

    print("Resultado final:")
    print(c)
