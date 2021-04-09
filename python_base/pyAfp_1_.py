
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
#______________________

#! Conditional Operators 
#? Comparing ordinal values
print(ord('a'))
print(ord('z'))

print('a'>'z')

print(7.0 == 7) #true

result = 6 == 6 # true
print(result)

#______________________

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

#______________________

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
#______________________





#! List and Tuples
x = [4,True, 'hi']
print(len(x)) # 3
x.extend([4,5,6,7,8]) #? extend is a loop with append
x.append('hello')
x.pop() # pop 'hello
x.pop(2) # removes 'hi
print("x[1]: ", x[1])
x[1] = 'not True'
print("x[1]: ", x[1])


#? List [] as reference type
x= [4, True, 'hi']
y = x
#? to copy the List
z = x[:]
x[0] = 'hello'
print(x) # ['hello', True, 'hi']
print(y) # ['hello', True, 'hi']
print(z) # [4, True, 'hi']


#? Tuples are Lists but immutables (can not append, remove or change elements)
x=(0,0,2,2)
#x[0] = 5 #TypeError: 'tuple' object does not support item assignment

l = [[],((),[]), []]
#______________________
