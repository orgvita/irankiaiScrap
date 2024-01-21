import config

from src.irankiaiScrap.parsers.cat_item_parser import CatItemParser
from src.irankiaiScrap.tools.html_parsing import parse_html


class SelectItemsParser:
    def __init__(self, link):
        self.soup = parse_html(link)

    @property
    def articles(self):
        locator = config.ITEM
        # articles_tags = self.soup.select(locator)
        return [CatItemParser(e) for e in self.soup.select(locator)]
