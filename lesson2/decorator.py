import logging

logging.basicConfig(level=logging.INFO)

def log_dec(fx): # fx= is a function
    def mfx(*args, **kwargs):
        logging.info(f"Started {fx.__name__}") 
        fx(*args, **kwargs) 
        logging.info(f"Stopped {fx.__name__}") 
    return mfx

@log_dec
def add(a,b):
    print("Inside add")
    print(f"{a + b}")

@log_dec
def sub(a,b):
    return a - b

add(a=1,b=2)
