from functools import lru_cache


@lru_cache(maxsize=1000)
def f(N):
    if N == 1:
        return "1"
    else:
        return str(f(N - 1)) + " " + str(N) + " " + str(f(N - 1))


N = int(input())

print(f(N))
