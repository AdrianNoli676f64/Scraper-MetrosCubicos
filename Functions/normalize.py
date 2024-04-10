def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = (s.replace(a, b).replace(a.upper(), b.upper())).upper()
    return s


def sin_acentos(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = (s.replace(a, b).replace(a, b))
    return s


def location_normal(locatios):
    lista_locations = []
    for ubicacion in locatios:
        temp = []
        for letter in ubicacion:
            clean_letter = sin_acentos(letter)
            temp.append(clean_letter)
        location = ''.join(temp)
        lista_locations.append(location)
    return lista_locations
