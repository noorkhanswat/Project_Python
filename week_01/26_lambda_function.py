# lambda function in python with detail explaination and apply in different examples
# A lambda function is a small anonymous function that can take any number of arguments but can only have one expression. Lambda functions are often used for short, simple functions that are not intended to be reused elsewhere in the code. The syntax for a lambda function in Python is: lambda arguments: expression
# example 1: a simple lambda function that adds 10 to a given number
x = lambda a: a + 10  # This line defines a lambda function that takes one argument (a) and returns the result of adding 10 to that argument
print("Lambda function result:", x(5))  # This line calls the lambda function with the argument 5, which returns 15, and prints the result to the console
# example 2: a lambda function that multiplies two numbers
y = lambda a, b: a * b  # This line defines a lambda function that takes two arguments (a and b) and returns the result of multiplying them together
print("Lambda function result:", y(5, 3))  # This line calls the lambda function with the arguments 5 and 3, which returns 15, and prints the result to the console
# example 3: using a lambda function with the built-in sorted() function to sort a list of tuples based on the second element of each tuple
my_list = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_list = sorted(my_list, key=lambda x: x[1])  # This line sorts the my_list of tuples based on the second element of each tuple (the fruit name) using a lambda function as the key argument
print("Sorted list:", sorted_list)  # This line prints the sorted list of tuples to the console
# example 4: using a lambda function with the filter() function to filter out   even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # This line uses the filter() function to create a new list of even numbers from the original numbers list by applying a lambda function that checks if each number is divisible by 2 (i.e., even)
print("Even numbers:", even_numbers)  # This line prints the list of even numbers to the console    
