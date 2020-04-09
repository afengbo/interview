# 斐波那契数列
def fib(n): return 1 if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(4))
