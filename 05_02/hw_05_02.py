from typing import Callable
import re


def generator_numbers(text: str):
    income_pattern = r"\d+\.\d+"
    values  = (re.findall(income_pattern, text))      

    for value in values:
        yield value


def sum_profit(text: str, func: Callable):
    income = 0

    for value in generator_numbers(text):
        income += float(value)
    
    return income


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
