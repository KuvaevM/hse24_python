import threading
import multiprocessing
import time


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def fibonacci_sync(n):
    fibonacci(n)


def fibonacci_threading(n):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def fibonacci_multiprocessing(n):
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    n = 200000
    with open('artifacts/part_1_artifact.txt', 'w') as f:
        f.write("Synchronous execution:\n")
        start_time = time.time()
        for _ in range(10):
            fibonacci_sync(n)
        end_time = time.time()
        f.write(f"Synchronous: {end_time - start_time} seconds\n\n")

        f.write("\nThreading execution:\n")
        start_time = time.time()
        for _ in range(10):
            fibonacci_threading(n)
        end_time = time.time()
        f.write(f"Threading: {end_time - start_time} seconds\n\n")

        f.write("\nMultiprocessing execution:\n")
        start_time = time.time()
        for _ in range(10):
            fibonacci_multiprocessing(n)
        end_time = time.time()
        f.write(f"Multiprocessing: {end_time - start_time} seconds\n")
