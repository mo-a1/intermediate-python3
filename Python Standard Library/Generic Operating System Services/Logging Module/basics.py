import logging

# Logging levels

# DEBUG - value = 10 : Detailed information, typically of interest only when diagnosing problems.

# INFO - value = 20 : Confirmation that things are working as expected.

# WARNING - value = 30 : An indication that something unexpected happened, or indicative of some problem in the near
#                       future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR - value = 40 : Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL - value = 50 : A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s - %(filename)s ")

logging.debug(__name__)
logging.info(__name__)
logging.warning(__name__)
logging.error(__name__)
logging.critical(__name__)

# create acustom logger to log with another formate or to another log file

# 1- create logger
cst_logger = logging.getLogger(__name__)
cst_logger.setLevel(logging.INFO)

# 2- create a handler to handle our logger
handler = logging.FileHandler("logs_2.log")

# 3- create formatter for the handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s - %(name)s")

# 4- set the formatter to the handler
handler.setFormatter(formatter)

# 5- add the handler to the custom logger
cst_logger.addHandler(handler)

# now test it
cst_logger.warning("test our custom logger")
