# function parameter and return in python with detail explaination and apply in different examples
# In Python, you can define a function that takes parameters and returns a value. Parameters are the inputs to a function, and the return statement is used to send a value back to the caller of the function. The syntax for defining a function with parameters and a return value in Python is: def function_name(parameters): block return value   
# example 1: defining a function with parameters and a return value
def add(a, b):  # This line defines a function named add that takes two parameters, a and b
    return a + b  # This line is the block of code that will be executed when the add function is called, returning the sum of a and b
result = add(5, 3)  # This line calls the add function with the arguments 5 and 3, and stores the returned value (which is 8) in the variable result
print("Result:", result)  # This line prints the value of result, which is the sum of 5 and 3, to the console
# example 2: defining a function that calculates the area of a rectangle
def calculate_area(length, width):  # This line defines a function named calculate_area that takes two parameters, length and width
    return length * width  # This line is the block of code that will be executed when the calculate_area function is called, returning the product of length and width, which is the area of the rectangle
area = calculate_area(5, 3)  # This line calls the calculate_area function with the arguments 5 and 3, and stores the returned value (which is 15) in the variable area
print("Area of the rectangle:", area)  # This line prints the value of area, which is the area of the rectangle calculated from the length and width, to the console
# example 3: defining a function that checks if a number is even or odd
def is_even(num):  # This line defines a function named is_even that takes one parameter, num
    if num % 2 == 0:  # This line checks if the number is even by using the modulus operator to check if the remainder when num is divided by 2 is 0
        return True  # If the condition is true (the number is even), this line returns True
    else:  # This line starts an else block that will be executed if the condition in the if statement is false (the number is odd)
        return False  # If the number is odd, this line returns False
number = 4  # This line assigns the value 4 to the variable number
result = is_even(number)  # This line calls the is_even function with the argument number (which is 4), and stores the returned value (which is True) in the variable result
print(f"Is {number} even?", result)  # This line prints a message that includes the value of number and the result of the is_even function, indicating whether the number is even or not to the console
# example 4: defining a function that returns multiple values
def calculate(a, b):  # This line defines a function named calculate that takes two parameters, a and b
    sum_result = a + b  # This line calculates the sum of a and b and stores it in the variable sum_result
    product_result = a * b  # This line calculates the product of a and b and stores it in the variable product_result
    return sum_result, product_result  # This line returns both the sum_result and product_result as a tuple
sum_value, product_value = calculate(5, 3)  # This line calls the calculate function with the arguments 5 and 3, and unpacks the returned tuple into the variables sum_value and product_value
print("Sum:", sum_value)  # This line prints the value of sum_value, which is the sum of 5 and 3, to the console
print("Product:", product_value)  # This line prints the value of product_value, which is the product of 5 and 3, to the console    
