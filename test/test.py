import logging

# Configure logging
logging.basicConfig(filename='data/app.log', level=logging.INFO)

# Example log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')