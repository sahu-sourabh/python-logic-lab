# Write a program to print reverse of a number?

def reverse_the_number(number_to_be_reversed):
    # 1. Store the sign of the number_to_be_reversed
    sign = -1 if number_to_be_reversed < 0 else 1

    # 2. Work with the absolute (positive) value
    positive_number = abs(number_to_be_reversed)
    reversed_number = 0

    # 3. Strip digits from right to left
    while positive_number != 0:
        last_digit = positive_number % 10
        reversed_number = reversed_number * 10 + last_digit
        positive_number = positive_number // 10
    
    # 4. Reapply the sign to the final integer result and print
    print(f'Reverse of {number_to_be_reversed} is {reversed_number * sign}')

reverse_the_number(123) # o/p: 321
reverse_the_number(-123) # o/p: -321
reverse_the_number(120) # o/p: 21
# Alternative: Pythonic String Slicing Approach