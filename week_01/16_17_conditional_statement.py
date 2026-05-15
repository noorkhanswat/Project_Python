# Conditional Statements in Python with detail explaination 
# Conditional statements are used to perform different actions based on different conditions. In Python, we have several types of conditional statements, including if, elif, and else. These statements allow us to control the flow of our program and make decisions based on certain criteria.      
# if statement
x = 10
if x > 5:  
    print("x is greater than 5")  # This block of code will be executed if the condition x > 5 is true
# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")  # This block of code will be executed if the condition y > 5 is true
else:
    print("y is not greater than 5")  # This block of code will be executed if the condition y > 5 is false
# if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")  # This block of code will be executed if the condition z > 10 is true
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")  # This block of code will be executed if the condition z > 5 is true and the previous condition z > 10 is false
else:
    print("z is less than or equal to 5")  # This block of code will be executed if both previous conditions are false  
# nested if statement
a = 15
if a > 10:  
    if a < 20:
        print("a is between 10 and 20")  # This block of code will be executed if the condition a > 10 is true and the nested condition a < 20 is also true
    else:
        print("a is greater than or equal to 20")  # This block of code will be executed if the condition a > 10 is true but the nested condition a < 20 is false
else:
    print("a is less than or equal to 10")  # This block of code will be executed if the condition a > 10 is false

    