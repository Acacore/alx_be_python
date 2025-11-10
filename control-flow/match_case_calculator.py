import sys


num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
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

