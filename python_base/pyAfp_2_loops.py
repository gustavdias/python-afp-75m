

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
#______________________



x = [3,4,42,3,2,4]
i = 0
while i < 10:
    print(i,'run')
    i+=1

#! not working!!!

# while True:
#     print('run')
#     i+=1
#     if i == 10:
#         break

# while True:
#     print(i,'run')
#     i+=1
#     while True:
#         if i == 10:
#             print('end')
#             break


#! Slice Operator
x = [2,34,435,54,3,657,6,77,2]
y=[3,4,65,73,3,234,76,8,5]
s="hello"

#sliced = [start:stop:step]
sliced = x[0:3:2] #[2, 435]
sliced = y[:8] #[3, 4, 65, 73, 3, 234, 76, 8]
sliced = y[2:] #[65, 73, 3, 234, 76, 8, 5]
sliced = x[2:4:] #[435, 54]

# reverse a list
sliced = y[::-1] #[5, 8, 76, 234, 3, 73, 65, 4, 3]
print(sliced)

reversed_string = s[::-1]
print(reversed_string)


#! Sets - if you care if something exists or not (you don care about the postion or frequency)
# faster than list
# unique unordered colection of elements
x = [2,34,435,54,3,657,6,77,2]

y = set() #to create a empty set
# s={} creates dictionary
print(type({}))


s = {2,3,45,2}
s2 = {3,4,22,1}
s.add(5)
s.remove(3)
print(s)
print(4 in s)
print(s.union(s2)) #{1, 2, 3, 4, 5, 22, 45}
print(s.difference(s2)) #{2, 45, 5}
print(s.intersection(s2)) #set()


#! Dictionaries (map, hash table) - lie set, it uses a hash = very fast
x = {'key': [1,2]}

print(x['key']) #[1, 2]
x['key2']=5 # add
print(x)

print('key' in x) #True
print(x.values()) #dict_values([[1, 2], 5])
print(list(x.values())) #[[1, 2], 5]
print(list(x.keys())) #['key', 'key2']

del x['key']
print(list(x.keys())) #['key2']


#!
for key, value in x.items():
    print(key,value)


for key in x:
    print(key, x[key])


#! Comprehensions
# define a for loop inside a list
x = [x%5 for x in range(5)] 
print(x) #[0, 1, 2, 3, 4]
x = [0 for x in range(5)]

print(x) # [0, 0, 0, 0, 0]


# gives 5 lists with 100 zeros each
x = [[0 for x in range(100)] for x in range(5)]

print(x) 

# if i in the range of 100 is divisible by 5 put on the list
x = [i for i in range(100) if i%5 ==0]
print(x) 


#? Works for dictionaries
x = {i:0 for i in range(100) if i%5 ==0}
print(x) 

#? for set
x = {i for i in range(100) if i%5 ==0}
print(x) 

#? tuples (constructor) without tuple it is a generator object
x = tuple(i for i in range(100) if i%5 ==0)
print(x) 


#! Functions

def func():
    print('run')
    def func():
        print('hi')
    func()

func()


#  z=None optional parameters
def func2(x,y, z=None):
    print('Run')
    return x*y, x/y

r1, r2 = func2(7,1)

print(func2(5,6))
print(r1,r2)


# Unpack Operator / * Args and **Kwargs

def func3(x):
    def func2():
        print("func3: ", x)

    return func2()

print(func3(3))
# x=func3(3)
# x()
# print(func3(3)())

def func4(*args,**kwargs):
    pass
x = [1,23,32323,3343]

# unpack operator separates all the elements from a list or from a collection into individual elements
print(*x)  #*x means unpack  => 1 23 32323 3343

def func5(x,y):
    print(x,y)

pairs = [(1,2), (3,4)]
#? * is for Toples or List
for pair in pairs:
    # func5(pair[0],pair[1])
    func5(*pair)



#? for dictionaries use **
func5(**{'x': 2, 'y':5})
#* It does not need to be in the correct order so long as you name the arguments as the keys
func5(**{'y':5, 'x': 2})

# Imagine that you have a function where you don know how many arguments, positional or keyword arguments you want to accept.
# It allows you to pass a unlimited amount of regular and keyword arguments

def func6(*args, **kwargs):
    print(*args, kwargs)

func6(1,2,3,4,5, one=0, two=1)

#*___________

#! Scope and Global

x = 'tim'
y = "mary"

def func7(name):
    x = "name"
    global y
    y = 'jane'
    print(x, y)

print(x, y)
func7('changed')
print(x, y)


#! raise Exception('Bad') 
# In JS is throw???

#! Not working!!!!!!!!!
# raise Exception('Bad')

# raise Exception('bad')

# this is a base class, you can extend it when you get into object oriented programming
# raise FileExistsError("")

#! Handling Exceptions 

try:
    x = 7/0
#except:
except Exception as e:
    print(e)
#finally always run, good for clean up
finally:
    print('finally')


#! Lambda - one line anonymous function
x = lambda x,y: x +  5+y
print(x(2,32))


#! Map and filter
x = [1,234,3,2,3,6,34,6,8,22,34,56,7]

mp = map(lambda i:i *22,x)
print(list(mp))# convert map into list

# filter uses true or false
fil = filter(lambda i:i % 2 == 0,x)
print(list(fil))

def func8(i):
    i = i * 3
    return i % 2 == 0
fil2 = filter(func8,x)    
print(list(fil))

#! F strings python 3.6
tim = 89
x = f'hello {6+8} {tim}'
print(x)

raise Exception('Bad')

