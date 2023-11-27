import logging
from logging.handlers import SysLogHandler

syslogHost = 'localhost'
syslogPort = 514

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler = SysLogHandler(address='/dev/log')
handler = SysLogHandler(address=(syslogHost, syslogPort))
logger.addHandler(handler)

logging.debug('This is a debug message')
logger.info('This is a log message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
