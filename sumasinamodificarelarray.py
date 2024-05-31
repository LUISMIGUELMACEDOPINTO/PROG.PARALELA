import multiprocessing
def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")


if __name__ == "__main__":
    a = [1, 2, 3, 20, 5,10]
    b = [6, 7, 8, 9, 10,20]
    c = multiprocessing.Array('i', 6)  # Shared array

    processes = []
    for tid in range(6):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
