def f(n: int, k: int) -> int:
        if n == 0: #base case
            return 0
        else:
            return k + f(n-1, k)