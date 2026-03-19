  #  Task 1
  #  - Create a function that would swap the value of x and y using only x and y as variables.
  #  - x and y must be numeric.
  #  - Return -1 if x and y is not numeric, and
  #  - print the swapped values if both x and y are numeric.

def swap(x, y):
    # Check if both inputs are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print(f"One or both variables are not numeric.")
        return -1
    
    # The Pythonic way to swap without a third variable:
    # This uses tuple unpacking.
    x, y = y, x
    
    print(f"Swapped values: x = {x}, y = {y}")
    return x, y

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

result = swap("Apple", 10)
result = swap(9,17)