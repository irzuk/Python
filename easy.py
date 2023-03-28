from time import time
import multiprocessing as mp
from threading import Thread


def fib_fun(num):
    nums = [0, 1]
    for i in range(2, num + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums


levels = 10
big_val = 100000

if __name__== "__main__":
    result = open("artifacts/easy.log", "w")
    # sinc
    begin = time()
    for _ in range(levels):
        fib_fun(big_val)
    duration = time() - begin
    result.write("Sinc: " + str(duration) + '\n')
    # threads
    begin = time()
    threads = [Thread(target=fib_fun, args=(big_val, )) for _ in range(levels) ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    duration = time() - begin
    result.write("Threads: " + str(duration) + '\n')
    # processes
    begin = time()
    processes = [mp.Process(target=fib_fun, args=(big_val,)) for _ in range(levels) ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    duration = time() - begin
    result.write("Processes: " + str(duration) + '\n')