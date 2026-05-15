#looping over data structure dictionary in python with detail explaination and apply in different examples
# In Python, you can loop over a dictionary using a for loop. When you loop over a dictionary, you can iterate over its keys, values, or key-value pairs. The syntax for looping over a dictionary in Python is: for variable in dictionary: block
# example 1: iterating over dictionary keys
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:  # This line starts a for loop that iterates over each key in the my_dict
    print("Key:", key)  # This line is the block of code that will be executed for each key in the dictionary, printing the current key
# example 2: iterating over dictionary values
for value in my_dict.values():  # This line starts a for loop that iterates over each value in the my_dict using the values() method
    print("Value:", value)  # This line is the block of code that will be executed for each value in the dictionary, printing the current value
# example 3: iterating over dictionary key-value pairs
for key, value in my_dict.items():  # This line starts a for loop that iterates over each key-value pair in the my_dict using the items() method, unpacking the key and value into separate variables
    print("Key:", key, "Value:", value)  # This line is the block of code that will be executed for each key-value pair in the dictionary, printing the current key and its corresponding value
# example 4: creating a new dictionary with modified values
new_dict = {}
for key, value in my_dict.items():  # This line starts a for loop that iterates over each key-value pair in the my_dict using the items() method, unpacking the key and value into separate variables
    new_dict[key] = str(value)  # This line is the block of code that will be executed for each key-value pair in the dictionary, converting the value to a string and adding it to the new_dict with the same key
print("New Dictionary:", new_dict)  # This line prints the new dictionary that contains the same keys as the original dictionary but with all values converted to strings after the loop has completed      
