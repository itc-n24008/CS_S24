import logging

def devide(x1, x2):
    return x1 / x2

logging.basicConfig(filename='testlog', level=logging.WARNING, format='%(levelname)s:%(asctime)s:%(message)s')

try:
    ret = devide(10, 0)
except:
    logging.exception('text exception message')
logging.shutdown()
