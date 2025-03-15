# python decorator is a function that modifies the behavior of the another function without changing it's actual code 
# we use it for logging ,authentication and timing function 
# start a code 
def my_deccorator (func):
    def wrapper():
        print("executing the function ....")
        func()
        print("function execution completed !!")
    return wrapper
def say_hello():
    print("hello,world!!")
    
say_hello()