import sys


num1 = input('Enter the first number:')
num2 = input('Enter the second number:')
num1 = int(num1)
num2 = int(num2)
operation = input('Choose the operation (+, -, *, /): ')

if num2 == 0:
    print('Cannot divide by zero.')
    sys.exit(1)

else:
    match operation:
        case '+':
            result = num1 + num2
            print(f'The result is {result}.')

        case '-':
            result = num1 + num2
            print(f'The result is {result}.')

        case '*':
            result = num1 * num2
            print(f'The result is {result}.')

        case '/':
            result = num1 / num2
            print(f'The result is {result}.')

        case _:
            print('Incorrect Input')

