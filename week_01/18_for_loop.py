# for loop  with detail explaination and apply in different examples
# A for loop is a control flow statement that allows you to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The syntax for a for loop in Python is: for variable in sequence: block
#where i can't used for loop in python
# for loops are typically used when you want to iterate over a sequence of items, such as a list, tuple, string, or range. However, there are certain situations where using a for loop may not be appropriate or necessary. For example:
# 1. When you need to perform a specific number of iterations that is not based on a sequence, you might use a while loop instead
# 2. When you need to iterate over a sequence of items but also need to modify the sequence while iterating, a for loop may not be suitable, and you might need to use a while loop or a different approach to avoid modifying the sequence during iteration
# 3. When you need to perform a task that does not involve iterating over a sequence, such as a simple conditional statement or a function call, a for loop may not be necessary and could be replaced with a more straightforward approach     
# example 1: iterating over a list
my_list = [1, 2, 3, 4, 5]
for item in my_list:  # This line starts a for loop that iterates over each item in the my_list
    print("Item:", item)  # This line is the block of code that will be executed for each item in the list, printing the current item
# example 2: iterating over a string
my_string = "Hello"
for char in my_string:  # This line starts a for loop that iterates over each character in the my_string
    print("Character:", char)  # This line is the block of code that will be executed for each character in the string, printing the current character
# example 3: iterating over a range of numbers
for i in range(5):  # This line starts a for loop that iterates over a range of numbers from 0 to 4 (5 is exclusive)
    print("Number:", i)  # This line is the block of code that will be executed for each number in the range, printing the current number
# example 4: iterating over a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:  # This line starts a for loop that iterates over each key in the my_dict
    print("Key:", key, "Value:", my_dict[key])  # This line is the block of code that will be executed for each key in the dictionary, printing the current key and its corresponding value   
