from bs4 import BeautifulSoup
import requests
import time

import config


def parse_html(url):
    time.sleep(config.SLEEP)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
