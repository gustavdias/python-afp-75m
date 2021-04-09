def f1():
    print('called f1')

def f2(f):
    f()

f1()
print(f1) #* Add "{installation home}/bin" to your PATH environment variable - it means that f1 is a object and it can be passed around 

f2(f1) #* called f1 - since we can represent functions as objects

#_________________________
#? wrapper function
def f3(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper

def f():
    print("Hello")

#f3(f) 
# this doesn't work  - You get nothing - You call a function f3() and it returns wrapper
print("print of f3(f): ",f3(f))
#? To call the function f():
f3(f)() #! This extra () allows you to decorate a function
# Started
# Hello
# Ended

#? Each time I call f, I want it to do the functionality of f3
x = f3(f) #! Function aliasing - changing the name of the function and changing the functionality 
x()


#! Function Decorators 
# #? You can substitute the above with: 
@f3
def fdec():
    print('decorator')

#? it writes this line for us x = f3(f) - no need for it anymore, so every time you call fdec, it will call f3 and pass the function f as a parameter to that
fdec()


@f3
def fdec2(a, b=9):
    print(a, b)

#? it writes this line for us x = f3(f) - no need for it anymore, so every time you call fdec, it will call f3 and pass the function f as a parameter to that
fdec2('right_decorator')


#? For it to work you have to use *args, **kwargs - the wrapper function will have a certain amount of arguments, we don know what the arguments will be, same for func() 
 #* without  *args, **kwargs  you get => TypeError: wrapper() takes 0 positional arguments but 1 was given
    # def wrapper(*args, **kwargs):
    #     func(*args, **kwargs)
    # before it was empty

#_________________________


#! Returning values from decorated functions


def f4(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val2 = func(*args, **kwargs)
        print("Ended")
        return val2

    return wrapper

@f4
def fi(t, v=12):
    print(t,v)

@f4
def add(x,y):
    return x+y

print(add(4,5))

#_________________________
#! decorators for methods
import time

def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print("After")

    return wrapper

#? You can use decorators for a method
class Test:
    @before_after
    def decorated_method(self):
        print('run')

t = Test()
t.decorated_method()
#_________________________


#! time decorator 
# How long it takes for a function or a method to run
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print('Function took: ', time.time() - before, "seconds")

    return wrapper

@timer
def run():
    time.sleep(2)

run()

#_________________________
#! log decorator - tells you when you've called a function with what specific arguments (in this case keyword arguments) and at what time and save that into a log file

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + "at")
        val = func(*args, ** kwargs)
        return val 
    
    return wrapper

@log
def run2(a,b,c=9):
    print(a+b+c)

run2(1,3, c=9)
