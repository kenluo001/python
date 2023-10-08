from operator import *


def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow
    }[k](a, b)


calculator(1, 2, '+')  # 3
calculator(3, 4, '**')  # 81