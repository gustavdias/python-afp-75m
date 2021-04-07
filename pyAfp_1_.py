
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

#! for loop
for i in range(2,34,3):
    print(i)

# stop
# start, stop
# start, stop, step 

for i in range(-10,-1,-1): # since you already passed -1, you get nothing
    print(i)

#? loop through a list
for i in [3,4,42,3,2,4]:
    print(i)



x = [3,4,5,6,78,8]
for i in range(len(x)):
    print(x[i])

#? enumerates creates indexes and values for the list
for i, element in enumerate(x):
    print(i,element)


#42m22s