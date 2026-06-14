try:
    num = int(input("Enter a number"))
    if num > 9:
        raise IndexError
except ValueError as e:
    print("Entered value is not a valid number")
except IndexError as e:
    print("Enter a valid index")

def add (a,b):
    try:
        return a+b
    except:
        print("Failed")
    finally:
        print("In finally block now")

import logging
logging.basicConfig(level=logging.INFO)
def log_dec(fx):
    def mfx(*args, **kwargs):
        logging.info(f"Starting function {fx.__name__}")
        fx(*args, **kwargs)
        logging.info(f"Finished executing {fx.__name__}")
    return mfx

@log_dec
def greet():
    print("Hello")

greet()