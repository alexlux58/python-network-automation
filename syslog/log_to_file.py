import logging

# Configure logging to write to a file
logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Additionally, setting up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
