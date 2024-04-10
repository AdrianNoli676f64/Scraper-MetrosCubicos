"""
Scraper for properties on sale in the page https://www.mercadolibre.com.mx/l/metroscubicos

The data on this page its accesible for anyone whitout an account
"""

## Manejo de datos
import numpy as np
import pandas as pd

## Herramientas para el Web scraping
import requests
from bs4 import BeautifulSoup
import cfscrape
import time
from time import sleep
import random
import cfscrape

## Limpieza, fechas, optimizadores y barras
import re
from datetime import datetime
from datetime import date
from tqdm import tqdm 

### librerias para el web scraping particular de inmuebles
import Functions.scraping as ws

scraper = cfscrape.create_scraper()