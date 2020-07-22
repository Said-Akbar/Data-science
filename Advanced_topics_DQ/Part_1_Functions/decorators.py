# 7/22/2020 Saidakbar P
# decorators modify the behavior of functions.

# functions as objects 
def has_docstring(func):
    """Check to see if the function 
    `func` has a docstring.
  
    Args:
        func (callable): A function.
    
    Returns:
        bool
    """
    ok = func.__doc__ is not None
    if not ok:
        print("{} doesn't have a docstring!".format(func.__name__))
    else:
        print("{} looks ok".format(func.__name__))
    return func.__doc__ is not None

load_docstring = has_docstring(load_and_plot_data)
log_docstring = has_docstring(log_product)

# nesting functions
def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a,b):
            return a-b
        return subtract
   

    else:
        print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

# local, global, nonlocal vars 
x = 50
def two():
    global x
    x = 30
	
def three():
    x = 100
    def four():
        nonlocal x
        x = 2
    four()
    print(x)

two() # print 30
three() # prints 2

# closures keeps record of variables that are no longer in scope, but that a function needs in order to run.
def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))
    return new_func
    
my_func = return_a_func(2, 17)
print(len(my_func.__closure__))
print(my_func.__closure__[0].cell_contents)
print(my_func.__closure__[1].cell_contents)

# calling my_special_function from get_new_func
def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
        func()
    return call_func

new_func = get_new_func(my_special_function)

def my_special_function():
    print('hello')

new_func() # prints 'You are running my_special_function()' because new_func() still keeps records of the previous call

# now comes the decorators 
def multiply(a, b):
    return a * b

def double_args(func):
    def wrapper(a, b):
        # Call the passed in function, but double each argument
        return func(2*a, 2*b)
    return wrapper

new_multiply=double_args(multiply)
new_multiply(1,5)

import inspect

def print_args(func):
    sig = inspect.signature(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments # gets var names
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper
@print_args
def my_function(a, b, c):
    print(a + b + c)
    
my_function(1,2,3) # prints 'my_function was called with a=1, b=2, c=3' and result of 6




