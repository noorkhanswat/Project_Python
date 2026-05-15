# while loop with detail explaination and apply in different examples and where i can't used while loop in python
# A while loop is a control flow statement that allows you to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop in Python is: while condition: block
# where i can't used while loop in python
# while loops are typically used when you want to repeat a block of code as long as a certain condition is true. However, there are certain situations where using a while loop may not be appropriate or necessary. For example:
# 1. When you need to iterate over a sequence of items, such as a list, tuple, string, or range, a for loop may be more suitable than a while loop, as it provides a more concise and readable way to iterate over the items in the sequence
# 2. When you need to perform a specific number of iterations that is known beforehand, a for loop may be more appropriate than a while loop, as it allows you to specify the number of iterations directly in the loop header
# 3. When you need to perform a task that does not involve repeating a block of code based on a condition, such as a simple conditional statement or a function call, a while loop may not be necessary and could be replaced with a more straightforward approach     
# example 1: counting from 1 to 5
count = 1
while count <= 5:  # This line starts a while loop that will continue to execute as long as the condition count <= 5 is true
    print("Count:", count)  # This line is the block of code that will be executed in each iteration of the loop, printing the current value of count
    count += 1  # This line increments the value of count by 1 in each iteration, ensuring that the loop will eventually terminate when count exceeds 5
# example 2: calculating the factorial of a number
number = 5
factorial = 1
while number > 1:  # This line starts a while loop that will continue to execute as long as the condition number > 1 is true
    factorial *= number  # This line multiplies the current value of factorial by the current value of number, effectively calculating the factorial as the loop iterates
    number -= 1  # This line decrements the value of number by 1 in each iteration, ensuring that the loop will eventually terminate when number reaches 1
print("Factorial:", factorial)  # This line prints the final calculated factorial after the loop has completed
# example 3: validating user input
user_input = ""
while user_input.lower() != "exit":  # This line starts a while loop that will continue to execute as long as the user_input is not equal to "exit" (case-insensitive)
    user_input = input("Enter a command (type 'exit' to quit): ")  # This line prompts the user for input and updates the user_input variable with the user's response
    print("You entered:", user_input)  # This line prints the user's input in each iteration of the loop, allowing them to see what they entered before they decide to exit the loop    
    