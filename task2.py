import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Генерує всі числа з тексту
    pattern = r"\d+\.\d+|\d+"
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    #Повертає суму всіх дійсних чисел 
    return sum(func(text))


# Приклад використання
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, " \
    "доповнений додатковими надходженнями 27.45 і 324.00 доларів."

    total = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total}")   # 1351.46
