import csv
import re
import time

import config
from src.irankiaiScrap.parsers.cat_find_items import SelectItemsParser
from src.irankiaiScrap.tools.logger import logger


class SearchSession:
    def __init__(self, search_phrase):
        self.search_for = search_phrase
        self.base_url = f"{config.SITE_URL}{self.search_for}"
        self.extracted_data = []

    def pages_in_width(self):
        continue_pagination = True
        self.end_control = {}
        no = 1
        while continue_pagination:
            self.url = f'{self.base_url}#!/p={no}'
            print(self.url)
            logger.info(f'category page: {self.url}')
            self.category_page = SelectItemsParser(self.url)
            for i, item_in_page in enumerate(self.category_page.articles):
                time.sleep(config.SLEEP)
                if i == 0:
                    if self.end_control == item_in_page.all_info:
                        print("Scraping done. Now saving results to a csv file")
                        continue_pagination = False
                        break
                    else:
                        self.end_control = item_in_page.all_info
                self.extracted_data.append(item_in_page.all_info)
            no += 1

# Writing data to a results file
    def output_results(self):
        self.file_name = re.search(config.FILENAME_PATTERN, self.search_for).group(1)
        print(self.file_name)
        csv_file = f"{config.DIRECTORY}/{self.file_name}.csv"
        csv_columns = ["Product", "Price", "Link", "SKU"]
        try:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=csv_columns)
                writer.writeheader()
                for item in self.extracted_data:
                    writer.writerow(item)
            logger.info(f'Successfully saved to {csv_file}.')
        except IOError:
            print("I/O error")
            logger.error(f'Error writing to {csv_file}...')
