from bs4 import BeautifulSoup
import re


def listas (lista, page):
    if page == 'metroscubicos':
        for pictionary in lista:
            location = pictionary['x'][0]
            key = pictionary['y'][0]
            price = pictionary['z'][0]
            pictionary['ubicacion'] = location
            pictionary['key'] = key
            pictionary['precio'] = re.sub("[^0-9.]", "", price)
            
            value = pictionary['c'][0]
            m2 = re.sub("[^0-9]", "", value[:6])
            rooms = re.sub("[^0-9]", "", value[15:])
            pictionary['m2'] = re.sub("[^0-9.]", "", m2)
            pictionary['rooms'] = re.sub("[^0-9]", "", rooms)

def llaves(llave):
    keys = list()
    for key in llave:
        temporal_list = list()
        clean = re.sub("[^a-zA-ZáéíóúñÑ ]", "", key).lower()
        for letter in clean:
            number = ord(letter)
            temporal_list.append(number)
        keys.append(temporal_list)
    return keys


def homologador_alcaldia(alcaldia):
    replacements = (
        ("AlvaroObregón", "ALVARO OBREGON"), ("Coyoacán", "COYOACAN"),
        ("Tlalpan", "TLALPAN"), ("MiguelHidalgo", "MIGUEL HIDALGO"),
        ("GustavoAMadero", "GUSTAVO A MADERO"), ("CuajimalpaDeMorelos", "CUAJIMALPA DE MORELOS"),
        ("CuajimalpadeMorelos", "CUAJIMALPA DE MORELOS"),
        ("Iztapalapa", "IZTAPALAPA"), ("Cuauhtémoc", "CUAUHTEMOC"),
        ("Iztacalco", "IZTACALCO"), ("LaMagdalenaContreras", "MAGDALENA CONTRETAS"),
        ("MagdalenaContreras", "MAGDALENA CONTRETAS"),
        ("VenustianoCarranza", "VENUSTIANO CARRANZA"), ("Xochimilco", "XOCHIMILCO"),
        ("Azcapotzalco", "AZCAPOTZALCO"), ("BenitoJuárez", "BENITO JUAREZ"),
        ("Tláhuac", "TLAHUAC"), ("MilpaAlta", "MILPA ALTA"),
        ("Álvaro Obregón", "ALVARO OBREGON"),  ("Miguel Hidalgo", "MIGUEL HIDALGO"),
        ("Gustavo A Madero", "GUSTAVO A MADERO"),  ("Gustavo A. Madero", "GUSTAVO A MADERO"),
        ("Cuajimalpa De Morelos", "CUAJIMALPA DE MORELOS"), ("Cuajimalpa", "CUAJIMALPA DE MORELOS"),
        ("La Magdalena Contreras", "MAGDALENA CONTRETAS"),
        ("Magdalena Contreras", "MAGDALENA CONTRETAS"), ("Venustiano Carranza", "VENUSTIANO CARRANZA"), 
        ("Benito Juárez", "BENITO JUAREZ"), ("Benito Juarez", "BENITO JUAREZ"), 
        ("Milpa Alta", "MILPA ALTA"), ("Cuauhtemoc", "CUAUHTEMOC"),
        ("ÁlvaroObregónCDMX", "ALVARO OBREGON"), ("CoyoacánCDMX", "COYOACAN"),
        ("TlalpanCDMX", "TLALPAN"), ("MiguelHidalgoCDMX", "MIGUEL HIDALGO"),
        ("GustavoAMaderoCDMX", "GUSTAVO A MADERO"), ("CuajimalpaDeMorelosCDMX", "CUAJIMALPA DE MORELOS"),
        ("IztapalapaCDMX", "IZTAPALAPA"), ("CuauhtémocCDMX", "CUAUHTEMOC"),
        ("IztacalcoCDMX", "IZTACALCO"), ("LaMagdalenaContrerasCDMX", "MAGDALENA CONTRETAS"),
        ("MagdalenaContrerasCDMX", "MAGDALENA CONTRETAS"),
        ("VenustianoCarranzaCDMX", "VENUSTIANO CARRANZA"), ("XochimilcoCDMX", "XOCHIMILCO"),
        ("AzcapotzalcoCDMX", "AZCAPOTZALCO"), ("BenitoJuárezCDMX", "BENITO JUAREZ"),
        ("TláhuacCDMX", "TLAHUAC"), ("MilpaAltaCDMX", "MILPA ALTA"),
        ("BitoJuárez", "BENITO JUAREZ"), ("LaMagdalaContreras", "MAGDALENA CONTRETAS"),
        ("VustianoCarranza", "VENUSTIANO CARRANZA"), ("InmueblesGustavoAMadero", "GUSTAVO A MADERO"),
    )
    for a, b in replacements:
        alcaldia = (alcaldia.replace(a, b))
    return alcaldia


def remates(texto):
    buscar_remate = ['Remate', 'REMATE', 'remate']
    resultado = 'False'
    for unico in buscar_remate:
        test = (unico in texto)
        if test == True:
            resultado = (resultado + str(test)).replace('False', '', 1)
    return resultado