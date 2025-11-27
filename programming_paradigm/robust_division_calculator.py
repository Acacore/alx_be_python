def safe_divide(numerator, denominator):
    try:
        answer = f'The result of the division is {float(numerator)/float(denominator)}'
        return answer
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except TypeError:
        return "Error: Please enter numeric values only."