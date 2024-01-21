SITE_URL = 'https://www.irankiai.lt/'
CATEGORY_PATTERN = r'^https:\/\/www\.irankiai\.lt\/'
EXPLAIN_TEXT = '''Enter the product category by copying from the sample list or
by searching the website and entering the category's URL.
You can enter the full address or just the part following 'https://www.irankiai.lt/'
    
Examples:
    atskelimo-plaktukai
    https://www.irankiai.lt/elektriniai-pjuklai/rankiniai-juostiniai-metalo-pjuklai
    suktuvai-ir-greztuvai/akumuliatoriniai-suktuvai
    matavimo-prietaisai/lazeriniai-nivelyrai\n'''

# from category page extract items (separate products; goods; sercices)
ITEM = 'div.item-inner'
# category page: pagination area
LAST_PAGINATION = 'div.pages ol li a' #li:last-of-type div[class='toolbar-bottom'] a[title='Kitas']
LAST_PAGINA = 'li:last-of-type'

#item info from category page
NAME = 'div.product-name a'
PRICE = 'span.price'
LINK = 'div.product-name a' # attrb hre
# item info from inner page
SKU = 'p.attribute-sku span + span'

# do not irritate website
SLEEP = 0.2
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# only include second part (after slash) of search phrase
DIRECTORY = '../../results'
FILENAME_PATTERN = '(?:.*/)?(.+)'

#logging config
LOG_LEVEL = "INFO"  # use: "INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"
LOG_FORMAT = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_FILE = '../../logs/irankiai.log'