    #"""
    #Task 1
    #- Create a function that reverses a given string (s).
    #- s must be a string.
    #- Return the reversed string.
    #"""

def string_reverse(s):
    # Ensure the input 's' is actually a string
    if not isinstance(s, str):
        return "Error: Input must be a string."
    
    # Use slicing to reverse the string
    # [start:stop:step] -> [:: -1] means "start to end, stepping backwards"
    reversed_s = s[::-1]
    
    print(reversed_s)
    return reversed_s
    


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

string_reverse("Hello World")
string_reverse("Python")
