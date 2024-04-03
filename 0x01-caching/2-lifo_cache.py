#!/usr/bin/env python
""" Implement a FIFO cache algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assign to the dictionary the item value to the key"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            newest = self.pop()
            del self.cache_data[newest]
            print("DISCARD: {}".format(newest))
        self.newest.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
