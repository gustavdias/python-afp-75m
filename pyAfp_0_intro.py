
'''
JS vs Python
JS: true false helloWorld
Python: True False hello_world

console.log(x.length) 
print(len(x))


When this is done, do to python udemy S5L39
'''



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

print("teST_TEst".capitalize()) 

test = "teST_TEst"
test
print(test.count("t")) # count how many t
print(test.lower().count("t")) # count how many t

#? String multiplication and string adition 
b = 'hello'
c = 3
print(b*c)
#! Conditional Operators 

#? Comparing ordinal values
print(ord('a'))
print(ord('z'))

print('a'>'z')

print(7.0 == 7) #true

result = 6 == 6 # true
print(result)

#! Chained Conditionals
x = 5
y = 7
z = 9

result1 = x==y # false
result2 = y>x # true
result3 = z<x +2 # false

# not result2 # false
result4 = result1 or not result2 or result3
print("result4: ", result4)


print(not(False or True)) # not True 

print(not(False and True)) # not False 
# 1st not
# 2nd and
# 3rd or
print(not(False and True or True)) #false

print("more than one >>: ", 2 < 3 > 10) # false
2 <= 3 >= 1 # true

#! if / else / elif

x = input('Name: ')
if x=='Tim':
    print('You are great!')
    print() # gives space
elif x == "Joe":
    print('Bye Joe')

else:
    print('you are not great')

print('Always do this')
