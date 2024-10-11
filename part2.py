def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Math Error!"

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

multiplication_result = multiply_numbers(num1, num2)
division_result = divide_numbers(num1, num2)

print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")
print(f"The division of {num1} by {num2} is: {division_result}")
