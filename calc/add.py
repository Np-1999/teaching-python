import logging
def add(a, b):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__) # __name__ name of current module
    handler = logging.FileHandler(f'{__name__}.log')  
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(f"Starting add run with a= {a}, b={b}")
    return a + b
