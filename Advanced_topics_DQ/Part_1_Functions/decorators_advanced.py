# 7/22/2020 Saidakbar P
# decorators advanced

# This decorator counts the number of times a function was used in the code
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)
    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')

foo()
foo()

print('foo() was called {} times.'.format(foo.count))

# this decorator will return function's data type
def print_return_type(func):
    # when print_return_type is called, it will call wrapper function and pass func args, kwargs 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))
        return result
    return wrapper

#foo() is not called here, the decorator calls it and checks its return type
@print_return_type
def foo(value):
    return value

print(foo(42))
print(foo([1,2,3]))
print(foo({'a': 42}))

# timer to check run time
def timer(func):
    """A decorator that prints how long a function took to run."""  
    def wrapper(*args, **kwargs):
        t_start = time.time()
    
        result = func(*args, **kwargs)
    
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
    
        return result
    return wrapper
@timer
def sleep_n_seconds(n=10):
    """Pause processing for n seconds.
  
    Args:
        n (int): The number of seconds to pause for.
    """
    time.sleep(n)

print(sleep_n_seconds.__doc__)
print(sleep_n_seconds.__name__)

# metadata
from functools import wraps

def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@add_hello # prints just 'hello'
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)
print_sum(10,20)
print(print_sum.__doc__)

def run_n_times(n): # a decorator that accepts an argument
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@run_n_times(3) # runs wrapper 3 times
def print_sum(a, b):
    print(a + b)
    
@run_n_times(5) # runs wrapper 5 times
def print_hello():
    print('Hello!')
    
print_sum(3,5) # print '8' 3 times
print_hello() # prints 'Hello!' 5 times

# a decorator that raises error when the function runs for more than 20 seconds
import signal
def timeout(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set an alarm for 5 seconds
            signal.alarm(n)
            try:
                # Call the decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(20) 
def bar():
    time.sleep(10)
    print('bar!')
    
bar() # prints 'bar!'

# assigns tags to functions
def tag(*tags):
    # Define a new decorator to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
            
        return wrapper
    # Return the new decorator
    return decorator

@tag('test', 'this is a tag')
def foo():
    pass

print(foo.tags) # prints ('test', 'this is a tag')
