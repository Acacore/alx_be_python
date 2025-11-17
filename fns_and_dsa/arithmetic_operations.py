from typing import Literal



def perform_operation(num1, num2, operation):
    ...
 
def perform_operation(num1: float, num2: float, operation: Literal["add", "subtract", "multiply", "divide"]):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2