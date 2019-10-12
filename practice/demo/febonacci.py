import sys
# yield生成器，返回迭代器对象
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
f=fib(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

