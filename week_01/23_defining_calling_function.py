#defining and calling function in python with detail explaination and apply in different examples
# A function is a block of reusable code that performs a specific task. In Python, you can define a function using the def keyword, followed by the function name and parentheses. The syntax for defining a function in Python is: def function_name(parameters): block
# example 1: defining and calling a simple function
def greet():  # This line defines a function named greet that takes no parameters
    print("Hello, World!")  # This line is the block of code that will be executed when the greet function is called, printing "Hello, World!" to the console
greet()  # This line calls the greet function, which executes the block of code defined in the function and prints "Hello, World!" to the console
# example 2: defining and calling a function with parameters
def add(a, b):  # This line defines a function named add that takes two parameters, a and b
    return a + b  # This line is the block of code that will be executed when the add function is called, returning the sum of a and b
result = add(5, 3)  # This line calls the add function with the arguments 5 and 3, and stores the returned value (which is 8) in the variable result
print("Result:", result)  # This line prints the value of result, which is the sum of 5 and 3, to the console
# example 3: defining and calling a function with default parameters
def greet(name="Guest"):  # This line defines a function named greet that takes one parameter, name, with a default value of "Guest"
    print(f"Hello, {name}!")  # This line is the block of code that will be executed when the greet function is called, printing a greeting message that includes the value of name to the console
greet()  # This line calls the greet function without providing an argument, so it uses the default value "Guest" and prints "Hello, Guest!" to the console     
greet("Alice")  # This line calls the greet function with the argument "Alice", which overrides the default value and prints "Hello, Alice!" to the console     
# example 4: defining and calling a function with variable-length arguments
def sum_all(*args):  # This line defines a function named sum_all that takes a variable number of arguments using *args
    total = 0  # This line initializes a variable total to 0, which will be used to accumulate the sum of all arguments
    for num in args:  # This line starts a for loop that iterates over each argument passed to the function (stored in args)
        total += num  # This line adds the current argument (num) to the total variable
    return total  # This line returns the final value of total, which is the sum of all arguments passed to the function
result = sum_all(1, 2, 3, 4, 5)  # This line calls the sum_all function with the arguments 1, 2, 3, 4, and 5, and stores the returned value (which is 15) in the variable result
print("Sum of all numbers:", result)  # This line prints the value of result, which is the sum of 1, 2, 3, 4, and 5, to the console
