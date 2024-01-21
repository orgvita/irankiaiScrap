import logging

import config

logging.basicConfig(format=config.LOG_FORMAT,
                    datefmt=config.LOG_DATEFMT,
                    level=config.LOG_LEVEL,
                    filename=config.LOG_FILE)

logger = logging.getLogger('scraping')