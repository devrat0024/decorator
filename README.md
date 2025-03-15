This project demonstrates the use of Python decorators, which allow us to modify the behavior of a function without changing its actual code.
Why Use Decorators?
Decorators are useful for:
Logging: Tracking function execution.
Authentication: Controlling access to functions.
Timing Functions: Measuring execution time.
Code Explanation:
The provided code defines a simple decorator function that wraps another function and adds execution messages before and after its call.
Code:
# Decorator function
def my_decorator(func):
    def wrapper():
        print("Executing the function ....")
        func()
        print("Function execution completed !!")
    return wrapper
# Applying the decorator:
@my_decorator
def say_hello():
    print("Hello, world!!")
# Calling the function
say_hello()
Expected Output:
Executing the function ....
Hello, world!!
Function execution completed !!
How to Run the Code:
Copy the code into a Python file (e.g., decorator_example.py).
Run the script using Python:
python decorator_example.py
Observe how the decorator modifies the function behavior.
Conclusion:
This example shows how decorators can be used to extend function behavior without modifying the original function code. Decorators are powerful tools in Python programming, commonly used in logging, authentication, and performance measurement.
