import logging

logging.basicConfig(level=logging.INFO, filename="log2.log", filemode="w", format="%(asctime)s - %(name)s - %(levelname)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error") 
logging.critical("critical")

# job
l1 = [1,2,3,0]

try:
    for num in l1:
        logging.debug("I am debug")
        10 / 0
except Exception as e:
    logging.error("Division By zeor", exc_info=True )

print("I am here to resolve")


import os 

env = os.environ("env") # env dev, prod

if env == "dev"
    set logging to debug
elif env =="prod"
    set logging to info


    Production failed
    info error crictilat
    
