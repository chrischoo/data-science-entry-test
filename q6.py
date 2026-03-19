    #"""
    #Task 1
    #- Create a function that finds the first negative number in a list (lst).
    #- Return the first negative number if found, otherwise return "No negatives".
    #- Use a while loop to implement this.
    #"""

def find_first_negative(lst):
# Ensure the input is a list
    if not isinstance(lst, list):
        return "Error: Input must be a list."
    
    index = 0
    # Loop as long as the index is within the bounds of the list
    while index < len(lst):
        # Check if the current element is negative
        if lst[index] < 0:
            print(f"The first negative {lst[index]} was found.")
            return lst[index]
        
        # Increment the index to check the next element
        index += 1
    
    # If the loop finishes without returning, no negative was found
    print(f"No negatives")
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

find_first_negative ([3,5,-1,7,-2,8])
find_first_negative ([2,10,7,0])