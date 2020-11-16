from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):
# check that the input is positive int
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

# compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

for n in range (1, 101):
    print(n, ":", fib(n))