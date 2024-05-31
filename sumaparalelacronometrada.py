import multiprocessing
import numpy as np
import time

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]

if __name__ == "__main__":
    # Generar arrays aleatorios usando NumPy
    a = np.random.randint(10, size=5)
    b = np.random.randint(10, size=5)
    c = multiprocessing.Array('i', 5)  # Shared array

    start_time = time.time()

    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    print("Resultado final:")
    print(c[:])
    print("Tiempo de ejecución:", end_time - start_time, "segundos")
