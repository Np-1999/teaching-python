import logging


logging.basicConfig(filename="log.log",level=logging.INFO, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


try:
        10 /0
except ZeroDivisionError as e:
        logging.error("ZeroDivisionError", exc_info=True)
