def greet(fxn):
    def mfx():
        print("Hello")
        fxn()
        print("Goodbye , THANKS FOR USING THIS DECORATOR FUNCTION")
    return mfx
@greet
def hello():
    print("Welcome to the world of Python Decorators!")
# greet(hello)()  # This is how you would call the decorated function without using the @ syntax
hello()

#import logging
#def log_decorator(func):
#    def wrapper(*args, **kwargs):
#        logging.info(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}")
#        result = func(*args, **kwargs)
#        logging.info(f"Function {func.__name__} returned: {result}")
#        return result
#    return wrapper
