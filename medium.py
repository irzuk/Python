from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from time import time
import math
from multiprocessing import cpu_count

def integrateThreads(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0

    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrateProcesses(f, a, b, *, n_jobs=1, n_iter=1000, ):
    acc = 0

    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

if __name__ == "__main__":
    result = open("artifacts/easy.log", "w")
    for n_jobs in range(2 * cpu_count()):

        begin = time()
        integrateThreads(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        duration = time() - begin
        result.write("Thread " + str(n_jobs)+ " jobs: " + str(duration) + '\n')

        begin = time()
        integrateThreads(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        duration = time() - begin
        result.write("Thread " + str(n_jobs) + " jobs: " + str(duration) + '\n')



