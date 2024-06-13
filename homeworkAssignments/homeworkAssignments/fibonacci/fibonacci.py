# fibonacci(n) = first + second

def fibonacci(nth):
    if nth == 2 or nth == 3:
        return 1
    elif nth == 1:
        return 0

    first = 1
    second = 1
    count = 3
    fib = first + second

    while count != nth:
        count += 1
        first = second
        second = fib
        fib = first + second

    return fib

print(fibonacci(10))