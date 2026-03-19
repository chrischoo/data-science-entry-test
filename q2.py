# Task 1
# - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
# - lst must be a list.
# - Return the modified list.

def find_and_replace(lst, find_val, replace_val):
    
    # Ensure the input 'lst' is actually a list
    if not isinstance(lst, list):
        return "Error: The first argument must be a list."
    
    # Iterate through the list using the range and length
    # to modify the elements in place via their index
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
            
    
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

my_list = [1, 2, 3, 4, 2, 2]
updated_list = find_and_replace (my_list, 2, 5)
print (updated_list)

my_list = ["apple", "banana", "apple"]
updated_list = find_and_replace (my_list, "apple", "orange")
print (updated_list)