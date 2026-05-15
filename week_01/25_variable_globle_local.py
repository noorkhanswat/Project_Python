# variable scope in python with detail explaination and apply in different examples
# In Python, variable scope refers to the region of a program where a variable is defined and can be accessed. There are three main types of variable scope in Python: global scope, local scope, and nonlocal scope. Understanding variable scope is important for writing clean and efficient code, as it helps to avoid naming conflicts and ensures that variables are used in the appropriate context.      
# global scope
x = 10  # This variable x is defined in the global scope, which means it can be accessed from anywhere in the program
def print_global_x():
    print("Global x:", x)  # This line accesses the global variable x and prints its value
print_global_x()  # This line calls the function print_global_x, which will print the value of the global variable x to the console
# local scope
def local_scope_example():
    y = 5  # This variable y is defined in the local scope of the function local_scope_example, which means it can only be accessed within this function
    print("Local y:", y)  # This line accesses the local variable y and prints its value
local_scope_example()  # This line calls the function local_scope_example, which will print the value of the local variable y to the console
# trying to access local variable outside its scope will result in an error
# print(y)  # This line will raise a NameError because y is not defined in the global scope and cannot be accessed outside of the local_scope_example function
# nonlocal scope
def outer_function():
    z = 20  # This variable z is defined in the local scope of the outer_function, which means it can only be accessed within this function and any nested functions
    def inner_function():
        nonlocal z  # This line declares that we want to use the nonlocal variable z from the outer_function
        z += 5  # This line modifies the value of the nonlocal variable z by adding 5 to it
        print("Inner z:", z)  # This line accesses the modified nonlocal variable z and prints its value
    inner_function()  # This line calls the inner_function, which will modify and print the value of z
    print("Outer z:", z)  # This line accesses the modified nonlocal variable z and prints its value after the inner_function has been called
outer_function()  # This line calls the outer_function, which will execute the code that demonstrates the use of nonlocal variables and print the modified value of z to the console        
