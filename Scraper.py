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
import time
from time import sleep
import random

## Limpieza, fechas, optimizadores y barras
import re
from datetime import datetime
from datetime import date
from tqdm import tqdm 

### librerias para el web scraping particular de inmuebles
import Functions.scraping as ws
import Functions.cleaning_tools as ct


### Elementos a extraer de la página
RULES_SEARCH_PAGE = {
    'x': {'tag': 'span', 'class': 'ui-search-item__location-label'},
    'y': {'tag': 'div', 'class': 'ui-search-item__group__element ui-search-item__title-grid'},
    'z': {'tag': 'span', 'class': 'andes-money-amount__fraction'},
    'c': {'tag': 'div', 'class': 'ui-search-item__attributes-container-grid'}
}
## x: ubicación
## y: variable llave
## z: precio
## c: características


print('*************************************************************************************************')
print('                                       Casas en venta')
#########################################################################################################
##################                Generación de URL para casas en venta                ##################
#########################################################################################################
alcaldia_url_c_m2 = [
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/benito-juarez/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/alvaro-obregon/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/coyoacan/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/tlalpan/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/miguel-hidalgo/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/gustavo-a-madero/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/cuajimalpa-de-morelos/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/azcapotzalco/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/iztapalapa/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/cuauhtemoc/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/iztacalco/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/la-magdalena-contreras/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/milpa-alta/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/tlahuac/',
    'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/venustiano-carranza/', 'https://inmuebles.metroscubicos.com/casas/venta/distrito-federal/xochimilco/'
]
print('Generación de URLs por alcaldía')
url_listas_casas = list()
for url in tqdm(alcaldia_url_c_m2):
    firts = url + "_NoIndex_True"
    number = 1
    url_listas_casas.append(firts)
    for i in range (0,0):  ## el rango puede llegar hasta 41
        number += 48
        next_url = url + "_Desde_" + str(number) + "_NoIndex_True"
        url_listas_casas.append(next_url)


print('---------------------------------------------------------------------------------------------')
#########################################################################################################
##################                             Web Scraping                            ##################
#########################################################################################################
listing_soups = list()
features_list = []
print('Web scraping casas en venta de MetrosCubicos en proceso...')

ws.listling_scraping(url_listas_casas, listing_soups, features_list, RULES_SEARCH_PAGE, 'mc')

print('Web scraping finalizado')
print('---------------------------------------------------------------------------------------------')

print('limpieza y almacenado de datos...')

ct.listas(features_list, 'metroscubicos')