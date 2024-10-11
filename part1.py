
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

addition_result = add_numbers(num1, num2)
subtraction_result = subtract_numbers(num1, num2)

print(f"The addition of {num1} and {num2} is: {addition_result}")
print(f"The subtraction of {num1} and {num2} is: {subtraction_result}")
