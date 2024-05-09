from us_visa_approval.logger import logging
from us_visa_approval.exception import USvisaException
import sys

try:
    a= 1/"10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys) from e  

