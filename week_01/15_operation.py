#Python operations, arithmetic, comparison, logical, bitwise, assignment, identity, membership
# explain me the below code with each steps
# arithmetic operations
a = 10
b = 5
print("Addition:", a + b)  # Output: 15
print("Subtraction:", a - b)  # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)  # Output: 2.0
print("Floor Division:", a // b)  # Output: 2
print("Modulus:", a % b)  # Output: 0
print("Exponentiation:", a ** b)  # Output: 100000
# comparison operations
print("Equal to:", a == b)  # Output: False
print("Not equal to:", a != b)  # Output: True
print("Greater than:", a > b)  # Output: True
print("Less than:", a < b)  # Output: False
print("Greater than or equal to:", a >= b)  # Output: True
print("Less than or equal to:", a <= b)  # Output: False
# logical operations
x = True
y = False
print("AND:", x and y)  # Output: False
print("OR:", x or y)  # Output: True
print("NOT:", not x)  # Output: False   
# bitwise operations
c = 5  # In binary: 0101
d = 3  # In binary: 0011
print("Bitwise AND:", c & d)  # Output: 1 (In binary: 0001)
print("Bitwise OR:", c | d)  # Output: 7 (In binary: 0111)
print("Bitwise XOR:", c ^ d)  # Output: 6 (In binary: 0110)
print("Bitwise NOT:",   ~c)  # Output: -6 (In binary: 1010)
print("Bitwise Left Shift:", c << 1)  # Output: 10 (In binary: 1010)
print("Bitwise Right Shift:", c >> 1)  # Output: 2 (In binary: 0010)
# assignment operations
e = 10
e += 5  # Equivalent to e = e + 5
print("Addition Assignment:", e)  # Output: 15
e -= 3  # Equivalent to e = e - 3
print("Subtraction Assignment:", e)  # Output: 12       
e *= 2  # Equivalent to e = e * 2
print("Multiplication Assignment:", e)  # Output: 24
e /= 4  # Equivalent to e = e / 4
print("Division Assignment:", e)  # Output: 6.0 
e //= 2  # Equivalent to e = e // 2
print("Floor Division Assignment:", e)  # Output: 3.0   
e %= 2  # Equivalent to e = e % 2       
print("Modulus Assignment:", e)  # Output: 1.0
e **= 3  # Equivalent to e = e ** 3
print("Exponentiation Assignment:", e)  # Output: 1.0   
# identity operations
f = 10
g = 10  
print("Is:", f is g)  # Output: True
print("Is not:", f is not g)  # Output: False
# membership operations
my_list = [1, 2, 3, 4, 5]
print("In:", 3 in my_list)  # Output: True
print("Not in:", 6 not in my_list)  # Output: True  
