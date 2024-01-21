import config

from src.irankiaiScrap.tools.html_parsing import parse_html


class ItemDetailsParser:
    def __init__(self, link):
        self.soup = parse_html(link)

    @property
    def sku(self):
        self.item_sku = self.soup.select_one(config.SKU).string
        return self.item_sku
