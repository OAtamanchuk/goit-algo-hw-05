def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Якщо в кеші вже є — повертаємо
        if n in cache:
            return cache[n]

        # Рекурсивне обчислення
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання
if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))   # 55
    print(fib(15))   # 610
