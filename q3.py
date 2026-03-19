#   """
#   Task 1
#   - Create a function that updates a dictionary (dct) with a new key-value pair.
#   - If the key already exists in dct, print the original value, then update its value.
#   - Return the updated dictionary.
#    """
 
def update_dictionary(dct, key, value):
    
    # Ensure the input 'dct' is actually a dictionary
    if not isinstance(dct, dict):
        return "Error: The first argument must be a dictionary."
    
    # Check if the key exists before updating
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    # Update or add the key-value pair
    dct[key] = value
    
    return dct
 
# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

my_data = {}
update_dictionary(my_data, "name", "Alice")
print (my_data)

my_data = {"age":25}
update_dictionary(my_data, "age", 26)
print (my_data)
