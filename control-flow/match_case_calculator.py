import sys


num1 = input('Enter the first number:')
num2 = input('Enter the second number:')
num1 = int(num1)
num2 = int(num2)
oparation_type = input('Choose the operation (+, -, *, /)')

if num2 == 0:
    print('Cannot divide by zero.')
    sys.exit(1)

else:
    if oparation_type == '+':
        result = num1 + num2
        print(f'The result is {result}.')

    elif oparation_type == '-':
        result = num1 + num2
        print(f'The result is {result}.')

    elif oparation_type == '*':
        result = num1 * num2
        print(f'The result is {result}.')

    elif oparation_type == '/':
        result = num1 / num2
        print(f'The result is {result}.')

    else:
        print('Incorrect Input')

