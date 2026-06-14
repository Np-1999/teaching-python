try:
    num = int(input("Enter a number"))
    l1= [1,2,3]
    raise IndexError   
except ValueError as e:
    print("Enter a valid number")
except IndexError as e:
    print("Number does not exist in list")
except:
    print("None matched")
finally:
    print("i will run no matter what")


# Fact, dim, other
# Supports fact, dim

import logging
logging.basicConfig(level=logging.INFO)
table_type = "Other"
try:
    if table_type == "Other":
        raise ModuleNotFoundError
except ModuleNotFoundError:
    logging.error("Modulenotfound")
except Exception as e:
   logging.error("ModuleNotfocund", exc_info=True)