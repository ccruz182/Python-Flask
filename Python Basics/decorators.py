import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print("In the decorator")
        func()
        print("After the decorator")

    return function_that_runs_fun

@my_decorator
def my_function():
    print("I'm the function")

my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("IN")
            func(*args, **kwargs)
            print("OUT")

        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too(x, y):
    print(x + y)

my_function_too(3, 4)
