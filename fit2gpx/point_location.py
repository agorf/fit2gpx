from sys import argv

import geopy
from geopy.geocoders import Nominatim

class PointLocation:
    STRIPPED_PREFIXES = ['municipal unit of ', 'municipality of ', 'regional unit of ']
    STRIPPED_SUFFIXES = [' municipal unit', ' municipality', ' region', ' district', ' county']

    geolocator = Nominatim(user_agent=argv[0])

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def name(self):
        address = self.__reverse_geocode(self.longitude, self.latitude).raw.get('address', {})

        return self.__clean_name(
            address.get('village') or
            address.get('town') or
            address.get('city') or
            address.get('locality') or
            address.get('municipality') or
            address.get('county') or
            address.get('state')
        )

    def __reverse_geocode(self, longitude, latitude):
        return self.__class__.geolocator.reverse((latitude, longitude), language='en', exactly_one=True)

    def __clean_name(self, name):
        if name:
            return self.__clean_suffixes(self.__clean_prefixes(name))

    def __clean_prefixes(self, name):
        name_lower = name.lower()

        for prefix in self.__class__.STRIPPED_PREFIXES:
            if name_lower.startswith(prefix):
                return name[len(prefix):].strip()

        return name

    def __clean_suffixes(self, name):
        name_lower = name.lower()

        for suffix in self.__class__.STRIPPED_SUFFIXES:
            if name_lower.endswith(suffix):
                return name[:-len(suffix)].strip()

        return name
