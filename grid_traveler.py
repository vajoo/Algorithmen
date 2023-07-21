import time

def grid_traveler_without_memory(m, n):
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler_without_memory(m-1, n) + grid_traveler_without_memory(m, n-1)

def grid_traveler_with_memory(m, n, mem={}):
    if (m, n) in mem:
        return mem[(m, n)]
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    mem[(m, n)] = grid_traveler_with_memory(m-1, n, mem) + grid_traveler_with_memory(m, n-1, mem)
    return mem[(m, n)]

start = time.time()
print(grid_traveler_without_memory(13, 13))
stop = time.time()
print(stop - start)


start = time.time()
print(grid_traveler_with_memory(501, 500))
stop = time.time()
print(stop - start)