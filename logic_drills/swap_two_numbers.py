# Write a program to swap two numbers?

def using_backup_variable(a, b):
    backup_var = a # holds value of either a or b, only drawback we have used extra memory & processing power.
    a = b
    b = backup_var
    print(f"Using backup variable {a} & {b}")

def using_mathematical_operations(a, b):
    # optimized solution without using extra memory & processing power.
    a = a+b
    b = a-b
    a = a-b
    print(f"Using mathematical operations {a} & {b}")

def using_bitwise_operation(a,b):
    # Without using mathatical operations.
    # Most optimized because no coversion required from decimal to binary and vice versa.
    a = a^b # a Ex-OR b
    b = a^b # a Ex-OR b
    a = a^b # a Ex-OR b
    print(f"Using bitwise operations {a} & {b}")

using_backup_variable(0, 1)
using_mathematical_operations(0, 1)
using_bitwise_operation(0, 1)