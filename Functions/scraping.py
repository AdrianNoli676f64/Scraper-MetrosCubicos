
import requests
from bs4 import BeautifulSoup
import cfscrape
import time
from datetime import datetime
from datetime import date
import re
from time import sleep
import random
scraper = cfscrape.create_scraper()


def scrape_page(page_url):
    """Extrae el código HTML de una página"""
    
    answer = requests.get(page_url)
    content = answer.content
    soup = BeautifulSoup(content, features='html.parser')
    
    return soup

def extract_listing(page_url, tag, clase):
    """Extrae todos los listings que se encuentren en la página"""
    
    page_soup = scrape_page(page_url)
    listings = page_soup.findAll(tag, {"class": clase})

    return listings


def extract_data(soup, params):
    """Extraer los datos de cada listings"""
    
    if 'class' in params:
        elements_found = soup.find_all(params['tag'], params['class'])
    else:
        elements_found = soup.find_all(params['tag'])
        
    if 'get' in params:
        element_texts = [el.get(params['get']) for el in elements_found]
    else:
        element_texts = [el.get_text() for el in elements_found]
        
    
    return element_texts

def listling_scraping(url_lista, listing_soups, features_list, RULES_SEARCH_PAGE, page):
    if page == 'mc':
        for j in tqdm(range(len(url_lista))):
            raw = (extract_listing(url_lista[j], "h1", "ui-search-breadcrumb__title"))
            if raw == []:
                raw = ['nan']
                raw = raw[0]
            else:
                raw = raw[0].text.replace('Casas en Venta en',  '', 1).replace('Departamentos en Venta en',  '', 1).replace('Inmueblesen',  '', 1).replace('en',  '', 1).replace('Inmuebles',  '', 1)
            clean_alcaldia = re.sub("[^A-Za-záéíóúÁÉÍÓÚ]", "", raw)
            listing_soups = extract_listing(url_lista[j], "div", "ui-search-result__content-wrapper")
            for listing in listing_soups:
                features_dict = {}
                for feature in RULES_SEARCH_PAGE:
                    features_dict[feature] = extract_data(listing, RULES_SEARCH_PAGE[feature])
                    features_dict['alcaldia'] = clean_alcaldia
                    features_list.append(features_dict)
            time.sleep(random.uniform(2, 5))