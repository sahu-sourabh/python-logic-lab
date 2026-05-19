# Write a program to print the Factorial of a given number?
# NOTE: Factorial of 0 and 1 is 1, and of negative numbers is Undefined

def print_factorial(number):
    if number < 0:
        return None # or we can "raise ValueError('Factorial is not defined for negative numbers.')"
    result = 1
    original_number = number
    while number > 1:
        result = result * number
        number -= 1
    print(f'Factorial of {original_number} is {result}.')

print_factorial(0) # o/p: 1
print_factorial(1) # o/p: 1
print_factorial(5) # o/p: 120
print_factorial(10) # o/p: 3628800
print_factorial(-10) # o/p: Undefined