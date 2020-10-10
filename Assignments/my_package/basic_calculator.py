from math import pow


def calculate(expr: str):
    expr = expr.split()
    num1 = float(expr[0])
    sign = expr[1]
    num2 = int(expr[2])

    signs = {
        '/': num1 / num2,
        '*': num1 * num2,
        '-': num1 - num2,
        '+': num1 + num2,
        '^': pow(num1, num2)
    }

    return f'{signs[sign]:.2f}'
