import config
import re

from src.irankiaiScrap.parsers.item_page import ItemDetailsParser


class CatItemParser:

    def __init__(self, article):
        self.article = article

    @property
    def item_name(self):
        locator = config.NAME
        return self.article.select_one(locator).string

    @property
    def item_price(self):
        locator = config.PRICE
        price = self.article.select_one(locator).string
        price_dot = re.sub(',', '\.', price)
        pattern = r'(\d+\,?\d+?)'
        match = re.search(pattern, price_dot)
        if match:
            match = float(match.group(1))
        return match

    @property
    def item_link(self):
        locator = config.LINK
        self.link_tag = self.article.select_one(locator)
        self.link = self.link_tag.attrs.get('href','-')
        return self.link

    @property
    def item_inner(self):
        self.child = ItemDetailsParser(f'{self.link}')
        self.item_sku = self.child.sku
        return (self.item_sku)

    @property
    def all_info(self):
        all_data = {}
        self.article_dict = {
            "Product": self.item_name,
            "Price": self.item_price,
            "Link": self.item_link,
            "SKU": self.item_inner
        }
        return self.article_dict


