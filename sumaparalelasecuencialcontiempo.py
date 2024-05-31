import numpy as np
import time

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")
if __name__ == "__main__":
    # Generar arrays aleatorios usando NumPy
    a = np.random.randint(10, size=5)
    b = np.random.randint(10, size=5)
    c = np.zeros(5, dtype=int)  # Array para almacenar resultados

    start_time = time.time()

    # Ejecutar la función worker secuencialmente
    for tid in range(5):
        worker(tid, a, b, c)

    end_time = time.time()

    print("Resultado final:")
    print(c)
    print("Tiempo de ejecución:", end_time - start_time, "segundos")
