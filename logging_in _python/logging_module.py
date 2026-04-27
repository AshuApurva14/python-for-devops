"""
How to use logging module with its methods for logs?

"""

import logging

# logging.warning("This is warning log")
# logging.error("This is error log")
# logging.critical("This is critical log")

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is debug log")