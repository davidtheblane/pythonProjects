import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if (b == 0):
        print('Error: Divisão por zero não é permitido.')
        return None
    return a / b


def calculadora():
    try:
        calc_result = None

        number1 = float(input('Digite o primeiro número: '))
        operator = input('Digite o operador matemático:\n'
                         '(+)somar\n,'
                         '(-)subtrair\n,'
                         '(*)multiplicar\n,'
                         '(/)dividir\n')
        number2 = float(input('Digite o segundo número: '))

        if operator == '+':
            calc_result = somar(number1, number2)
        elif operator == '-':
            calc_result = subtrair(number1, number2)
        elif operator == '*':
            calc_result = multiplicar(number1, number2)
        elif operator == '/':
            calc_result = dividir(number1, number2)
        else:
            print('Entrada inválida. Por favor digite um operador válido.')

        print(f"Resultado das operações é: ${calc_result}")
        return calc_result

    except ValueError:
        print('Entrada inválida. Por favor digite apenas, números.')


calculadora()
