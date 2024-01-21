import re

import config
from src.irankiaiScrap.tools.find_products import SearchSession
from src.irankiaiScrap.tools.logger import logger


def what_category():
    print(config.EXPLAIN_TEXT)
    user_input = input('Enter HERE: ')
    category = re.sub(config.CATEGORY_PATTERN, '', user_input)
    logger.info(f'Products category: {category}. Scrapping started.')
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
