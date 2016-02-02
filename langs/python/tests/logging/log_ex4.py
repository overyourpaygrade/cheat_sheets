import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    open('/path/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True) 
