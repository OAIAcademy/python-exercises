import math
import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep, time


def task(delay, what):  # nothing special about the tasks
    sleep(delay)
    print(what)


def task_computation(delay):  # task with return value
    sleep(delay)
    return delay


def task_no_idle(cycles):
    now = time()
    var = 1
    while cycles > 0:
        cycles -= 1

    return time() - now


def main():
    now = time()
    task1 = threading.Thread(target=task, args=(10, '1 - 10 sec'))  # you can pass arguments as a tuple
    task2 = threading.Thread(target=task, args=(20, '1 - 20 sec'))
    task1.start()
    task2.start()
    task1.join()
    task2.join()
    print(f"total: {time() - now}")
    print("\nwith pool")
    pool = ThreadPoolExecutor(2)
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
    pool = ThreadPoolExecutor(2)
    now = time()
    results = pool.map(task_no_idle, [50000000, 100000000])
    for result in results:
        print(result)
    print(f"total: {time() - now}")


main()
