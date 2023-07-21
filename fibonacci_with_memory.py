def fib_without_memory(n):
    if n == 0 or n == 1:
        return n
    return fib_without_memory(n-1) + fib_without_memory(n-2)

def fib_with_memory(n, mem={}):
    if n in mem:
        return mem[n]
    if n == 0 or n == 1:
        return n
    mem[n] = fib_with_memory(n-1, mem) + fib_with_memory(n-2, mem)
    return mem[n]

print(fib_without_memory(33))
print(fib_with_memory(999))