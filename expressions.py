#VS, 7th period Integrers, Floats and Expressions notes.

# Interger IN PYTHON is a whole number!
people= 23
cars= 50
computers= 29
awareness= -12

# Float are numbers with decimals!
pi= 3.14159
temp= 95.6
cost= 1.99
rain= 2.17

#Arithmetic Operators: symbols you can use for math but while coding, things like 
# +  -  * /
#  //  **  %

print(f"18/4 is {18/4} or {18//4} with a remainder of {18%4}")
print(f"18/5 is {18/5} or {18//5} with a remainder of {18%5}")

# order of operations
average=(85+66+94+72)/4
print(f"The average is {average}")

grades= [85,66,94,72,100]
students= len(grades)
average= sum(grades)/students

print(f"the average is {int(average)}")

#inputs are always strings, you cannot do math with a string. If you want it to be able 
#do the math then convert to an interger OR a float

#convert the data type
price = float (input("how much did it cost?"))
tax = 0.0485
sales_tax= price*tax
total=price+sales_tax
print(f"Your total is {total}")