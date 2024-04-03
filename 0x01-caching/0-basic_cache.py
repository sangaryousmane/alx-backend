#!/usr/bin/python3
""" inherits from BaseCaching and implement a simple
caching system """
from base import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and implement a simple
    caching system """

    def put(self, key, item):
        """ Assign to the dictionary the item with
        the given key """

        if (key is None) or (item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dictionary linked to the
        key """
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data.get(key)
