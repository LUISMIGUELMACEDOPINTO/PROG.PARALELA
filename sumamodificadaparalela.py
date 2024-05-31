import multiprocessing
import numpy as np

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    # Generar arrays aleatorios usando NumPy
    a = np.random.randint(10, size=5)
    b = np.random.randint(10, size=5)
    c = multiprocessing.Array('i', 5)  # Shared array

    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
