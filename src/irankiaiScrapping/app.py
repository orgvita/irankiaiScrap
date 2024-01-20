import logging
import re

import config
from src.irankiaiScrapping.tools.find_products import SearchSession

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='../../logs/logs.txt')
logger = logging.getLogger('scraping')
logger.info('Loading items list...')

def what_category():
    print(config.EXPLAIN_TEXT)
    user_input = input('Enter HERE: ')
    category = re.sub(config.CATEGORY_PATTERN, '', user_input)
    return category

def scrape_site():
    category = what_category()
    scrape_session = SearchSession(category)
    scrape_session.pages_in_width()
    scrape_session.output_results()
    if input("Another search? Press 'y' or 'n' ") == 'y':
        scrape_site()


if __name__ == '__main__':
    scrape_site()
