#%% Decorator Function
import time

def Decorator_function(original_function):
    def Wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return Wrapper_function

@Decorator_function
def display():
    print('Display function ran')
@Decorator_function
def display_informations(name, age):
    print('display_informations function ran with arguments: ({}, {})'.format(name, age))
display_informations('Saif', 21)
display()
#%% Decorator Class
class Decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
@Decorator_class
def display():
    print('display function ran')
@Decorator_class
def display_informations(name, age):
    print('display_informations function ran with arguments: ({}, {})'.format(name, age))
display_informations('Saif', 21)
display()
#%% Practical examples
from functools import wraps
# example 1
def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs) )
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} seconds'.format(original_function.__name__, t2))
        return result
    return wrapper

@my_timer
@my_logger
def display_informations(name, age):
    time.sleep(1)
    print('display_informations function ran with arguments: ({}, {})'.format(name, age))
display_informations('Mohammed', 20)