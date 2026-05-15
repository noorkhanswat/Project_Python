# loop over data structure string in python with detail explaination and apply in different examples
# In Python, you can loop over a string using a for loop. When you loop over a string, you are iterating over each character in the string one by one. The syntax for looping over a string in Python is: for variable in string: block
# example 1: iterating over a string
my_string = "Hello, World!"
for char in my_string:  # This line starts a for loop that iterates over each character in the my_string
    print("Character:", char)  # This line is the block of code that will be executed for each character in the string, printing the current character
# example 2: counting the number of vowels in a string
vowels = "aeiouAEIOU"
count = 0
for char in my_string:  # This line starts a for loop that iterates over each character in the my_string
    if char in vowels:  # This line checks if the current character is a vowel by checking if it is in the vowels string
        count += 1  # If the character is a vowel, this line increments the count variable by 1 to keep track of the number of vowels found
print("Number of vowels:", count)  # This line prints the total number of vowels found in the string after the loop has completed
# example 3: creating a new string with only the uppercase letters from the original string
uppercase_string = ""
for char in my_string:  # This line starts a for loop that iterates over each character in the my_string
    if char.isupper():  # This line checks if the current character is an uppercase letter using the isupper() method
        uppercase_string += char  # If the character is uppercase, this line adds it to the uppercase_string variable
print("Uppercase letters:", uppercase_string)  # This line prints the new string that contains only the uppercase letters from the original string after the loop has completed     
