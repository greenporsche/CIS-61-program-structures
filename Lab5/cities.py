def make_city(name, lat, lon):
    return [name, lat, lon]

def get_name(city):
    return city[0]

def get_lat(city):
    return city[1]

def get_lon(city):
    return city[2]

from math import sqrt
def distance(city1, city2):
    return sqrt((get_lat(city1) - get_lat(city2))**2 + (get_lon(city1) - get_lon(city2))**2)

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    location = make_city("location", lat, lon)
    if distance(location, city1) < distance(location, city2):
        return get_name(city1)
    else:
        return get_name(city2)