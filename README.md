# Irankiai.lt Web Scraper

This Python project scrapes product category information from https://www.irankiai.lt. It navigates through all pages within a provided category to gather comprehensive product details.

## Features
- **Breadth and Depth Scraping**: Traverses through category pages and dives into individual product pages for detailed information.
- **CSV Output**: Extracted data is stored in the `results/` directory, with filenames like `productCategory.csv`.

## Getting Started
1. Navigate to `src/irankiaiScrap`.
2. Run `app.py` and follow the prompts to select a product category or input a direct URL.

## Requirements
- Python 3.11
- Modules: BeautifulSoup, requests, re and others (listed in `requirements.txt`)

## Configuration
Customize the scraping behavior in `config.py`, including:
- Logging level
- Sleep interval between page scrapes
- Output filename pattern
- Output directory

## Extensibility
If the website's structure changes, `config.py` allows for updates to XPath selectors to maintain accurate field extraction (like product name, price, and SKU).

## Installation
Ensure you have Python 3.11 installed and run `pip install -r requirements.txt` to install required modules.