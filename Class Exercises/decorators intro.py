# Define a simple function
def my_function():
    print("Executing my_function")

# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Decorate the function using the decorator
my_function = my_decorator(my_function)

# Call the decorated function
my_function()