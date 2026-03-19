    #"""
    #Task 1
    #- Create a function to check if the number (num) is divisible by another number (divisor).
    #- Both num and divisor must be numeric.
    #- Return True if num is divisible by divisor, False otherwise.
    #"""
    
def check_divisibility(num, divisor):
    # Ensure both inputs are numeric (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Error: Both arguments must be numeric."
    
    # Avoid DivisionByZero error
    if divisor == 0:
        return "Error: Cannot divide by zero."
    
    # Use the modulo operator to check the remainder
    if num % divisor == 0:
        print(f"Divisibility of {num} by {divisor} is OK");
        return True
    else:
        print(f"Divisibility of {num} by {divisor} is NOT OK");
        return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

check_divisibility (10, 2)
check_divisibility (7, 3)