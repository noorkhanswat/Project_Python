# nested loops in python with detail explaination and apply in different examples
# A nested loop is a loop that is contained within another loop. The inner loop will be executed for each iteration of the outer loop. Nested loops are often used to iterate over multi-dimensional data structures, such as lists of lists, or to perform complex iterations that require multiple levels of looping.
# The syntax for a nested loop in Python is:
# for variable in sequence:
#     for variable in sequence:
#         block
# example 1: iterating over a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   
for row in matrix:
    for element in row:
        print(element)
# example 2: printing a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # This line adds a blank line after each row of the multiplication table for better readability
# example 3: generating combinations of items from two lists
colors = ["red", "green", "blue"]
shapes = ["circle", "square", "triangle"]
for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")
        