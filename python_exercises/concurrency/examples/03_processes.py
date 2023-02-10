import math
import multiprocessing
from multiprocessing import Process
from time import sleep, time


def task(delay, what):
    sleep(delay)
    print(what)


def task_computation(delay):
    sleep(delay)
    return delay


def task_no_idle(cycles):
    now = time()
    var = 1
    for i in range(1, cycles):
        var = math.sqrt(var ** i)
    return time() - now


def main():
    now = time()
    task1 = Process(target=task, args=(10, '1 - 10 sec'))  # you can pass arguments as a tuple
    task2 = Process(target=task, args=(20, '1 - 20 sec'))
    task1.start()
    task2.start()
    task1.join()
    task2.join()
    print(f"total: {time() - now}")
    print("\nwith pool")
    pool = multiprocessing.Pool(2)
    now = time()
    results = pool.map(task_computation, [5, 2])
    for result in results:
        print(result)
    print(f"total: {time() - now}")
    print("\nreal not-idle tasks")
    print("synch")
    now = time()
    print(task_no_idle(50000000))
    print(task_no_idle(100000000))
    print(f"total: {time() - now}")
    print("asynch")
    pool = multiprocessing.Pool(2)
    now = time()
    results = pool.map(task_no_idle, [50000000, 100000000])
    for result in results:
        print(result)
    print(f"total: {time() - now}")


if __name__ == '__main__':  # on Windows main guard is needed
    main()
