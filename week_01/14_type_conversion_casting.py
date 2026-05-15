# type conversion and casting in python
# type conversion is the process of converting one data type to another data type
# there are two types of type conversion: implicit and explicit

# implicit type conversion
a = 5
b = 10.0
c = a + b  # here python will implicitly convert integer to float
print("Implicit conversion:", c)

# explicit type conversion
d = "10"
e = "20"
f = int(d) + int(e)  # here we are explicitly converting string to integer
print("Explicit conversion:", f)

# casting is the process of converting one data type to another data type
# it is done using built-in functions like int(), float(), str(), etc.
g = 10
h = float(g)
i = str(h)
print("Casting:", g, h, i)