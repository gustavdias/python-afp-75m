
#/n go to the next line after this line is printed
print('Hello', "end", 87, False, end='|')
print('end of test1')

print('Hello', "end", 87, False, end='\n')
print('end of test2')

#-------------------

#!--- Variables
#? no special characters, can't start with number, name_like_this
hello = 'tim'
world = hello
hello = 'no'
hello_world32 = 0
print(hello, world)
#-------------------

#! User input
#Name = input('Name: ')#you need a string, and give space so stays as Name: username
#print(Name)
#-------------------

#! Arithmetic Operators
x=9 #integer
y=3 #integer
result = x/y # result is float, when you use /, the result is float
int(result)
exponent = x**y
print(exponent)

z=10
a=3
floor = z//a #gives the integer result of whatever the division is, removes all te decimal points
print(floor)

mod = z%a
print(mod)

#! Order of operations
# B - Brackets
# E - Exponents
# D - division
# M - Multiplication
# A - Adition
# S - Subtraction
# M - Mod %

#! Input 
num = input("Number: ") #str
num_flout = float(num) -5 # str to int

#! String Methods
print(type(num_flout))

hello = "hello".upper() # upper case
print(hello)
print(hello.lower()) # lower case

print(hello.lower()) 

#20m46s